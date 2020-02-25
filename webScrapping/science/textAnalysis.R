library(readr)
library(tidyr)
library(tm)
library(ggwordcloud)
library(ggplot2)
library(topicmodels)
library(dplyr)
library(tidytext)
library(reshape2)

#Antes de iniciar, definimos un tema personalizado para ggplot
theme_beautiful <- theme(
  text = element_text(family = "Quicksand", colour = "#353535"),
  title = element_text(family = "Raleway"),
  plot.title =  element_text(size = 18, hjust = 0.5),
  plot.subtitle = element_text(size = 13, hjust = 0.5),
  axis.text = element_text(size = 10),
  axis.title = element_text(size = 13),
  legend.title = element_text(size = 13),
  legend.text = element_text(size = 12)
)

#Cargamos en memoria los tweets
textoTesis <- read_csv("webScrapping/data/tesis.csv")

#Cargamos en memoria las stopwords en español
conn <- file("webScrapping/data/stopWords.txt", open = "r")
stopWords <- readLines(conn)
close(conn)

#Remover símbolos
stripSymbol <- function(x) gsub("[\x3F\x21\xBF\xA1\x2E\x22\x2F\x25\x3A\x3B\x3C\x3D\x3E\x3F]", "", x)

textoTesis$Tema <- str_split(textoTesis$Rubro, "[.]", simplify = TRUE)[,1]
textoTesis$Tema <- str_to_title(textoTesis$Tema)

#Creamos un corpus de términos
tesisCorpus <- Corpus(VectorSource(textoTesis$Texto)) %>%
  tm_map(content_transformer(tolower)) %>%
  tm_map(removePunctuation) %>%
  tm_map(removeWords, stopWords) %>%
  tm_map(stripWhitespace)

#Creamos un corpus de rurbos
rubroCorpus <- Corpus(VectorSource(textoTesis$Rubro)) %>%
  tm_map(content_transformer(tolower)) %>%
  tm_map(removePunctuation) %>%
  tm_map(removeWords, stopWords) %>%
  tm_map(stripWhitespace)

#Matriz de términos
MdT_Tesis <- TermDocumentMatrix(tesisCorpus) %>%
  removeSparseTerms(sparse = 0.999)
MdT_Rubro <- TermDocumentMatrix(rubroCorpus) %>%
  removeSparseTerms(sparse = 0.999)

#Términos más frecuentes
MdT_freq_Tesis <- rowSums(as.matrix(MdT_Tesis)) %>%
  sort(decreasing = T)
MdT_freq_Rubro <- rowSums(as.matrix(MdT_Rubro)) %>%
  sort(decreasing = T)

MdT_freq_Tesis
MdT_freq_Rubro

freq_temas <- table(textoTesis$Tema)
freq_temas <- as.data.frame(freq_temas, stringsAsFactors = F)
freq_temas[freq_temas$Freq > 10,]

#Número de rubros
length(MdT_freq_Tesis)
length(MdT_freq_Rubro)
length(unique(textoTesis$Rubro))

#Nube de palabras
plot_nubePalabras_Tesis <- ggplot() +
  geom_text_wordcloud_area(aes(label = names(MdT_freq_Tesis[MdT_freq_Tesis > 500]), size = MdT_freq_Tesis[MdT_freq_Tesis > 500],
                               colour = MdT_freq_Tesis[MdT_freq_Tesis > 500])) +
  scale_colour_viridis_c() +
  scale_size_area(max_size = 30) +
  ggtitle("Términos más frecuentes en el texto de las tesis capturadas (pleno, 9na y 10ma épocas)") +
  labs(caption = "Se omiten palabras vacías (stopwords).") +
  theme_minimal() +
  theme_beautiful
plot_nubePalabras_Rubros <- ggplot() +
  geom_text_wordcloud_area(aes(label = names(MdT_freq_Rubro[MdT_freq_Rubro > 50]), size = MdT_freq_Rubro[MdT_freq_Rubro > 50],
                               colour = MdT_freq_Rubro[MdT_freq_Rubro > 50])) +
  scale_colour_viridis_c() +
  scale_size_area(max_size = 30) +
  ggtitle("Términos más frecuentes en el rubro de las tesis capturadas (pleno, 9na y 10ma épocas)") +
  labs(caption = "Se omiten palabras vacías (stopwords).") +
  theme_minimal() +
  theme_beautiful
plot_nubePalabras_Temas <- ggplot() +
  geom_text_wordcloud_area(aes(label = freq_temas$Var1[freq_temas$Freq > 10], size = freq_temas$Freq[freq_temas$Freq > 10],
                               colour =freq_temas$Freq[freq_temas$Freq > 10])) +
  scale_colour_viridis_c() +
  scale_size_area(max_size = 20) +
  ggtitle("Temas más frecuentes en las tesis capturadas (pleno, 9na y 10ma épocas)") +
  labs(caption = "Se omiten palabras vacías (stopwords).") +
  theme_minimal() +
  theme_beautiful

plot_nubePalabras_Tesis
plot_nubePalabras_Rubros

ggsave("webScrapping/nubeTesis.png", plot = plot_nubePalabras_Tesis, scale = 2,
       width = 15, height = 10, units = "cm", dpi = 300, device = "png")
ggsave("webScrapping/nubeRubros.png", plot = plot_nubePalabras_Rubros, scale = 2,
       width = 15, height = 10, units = "cm", dpi = 300, device = "png")
ggsave("webScrapping/nubeTemas.png", plot = plot_nubePalabras_Temas, scale = 2,
       width = 15, height = 10, units = "cm", dpi = 300, device = "png")


matrix_Tesis <- as.DocumentTermMatrix(MdT_Tesis, sparce = T)
matrix_Rubros <- as.DocumentTermMatrix(MdT_Rubro, sparce = T)

lda_Tesis <- LDA(matrix_Tesis, k = 20,
                 control = list(verbose = 1, burnin = 100, iter = 500), method = "Gibbs")
lda_terms_Tesis <- tidy(lda_Tesis)
lda_terms_Tesis <- lda_terms_Tesis %>%
  group_by(topic) %>%
  top_n(10, beta) %>%
  ungroup() %>%
  arrange(topic, -beta) %>%
  mutate(term = reorder(term, beta))

lda_Rubros <- LDA(matrix_Rubros, k = 20,
                 control = list(verbose = 1, burnin = 100, iter = 500), method = "Gibbs")
lda_terms_Rubros <- tidy(lda_Rubros)
lda_terms_Rubros <- lda_terms_Rubros %>%
  group_by(topic) %>%
  top_n(10, beta) %>%
  ungroup() %>%
  arrange(topic, -beta) %>%
  mutate(term = reorder(term, beta))

plotLDA_Tesis <- ggplot(data = lda_terms_Tesis, aes(term, beta, fill = factor(topic))) +
  geom_col() +
  facet_wrap(~ topic, scales = "free", nrow = 3, ncol = 8) +
  coord_flip() +
  scale_fill_viridis_d() +
  ggtitle("Términos más probables por tema", subtitle = "Modelo LDA, k = 2500") +
  labs(fill = "Tema (k)", x = "Término", y = "β") +
  theme_minimal() +
  theme_beautiful

plotLDA_Rubros <- ggplot(data = lda_terms_Rubros, aes(term, beta, fill = factor(topic))) +
  geom_col() +
  facet_wrap(~ topic, scales = "free", nrow = 3, ncol = 8) +
  coord_flip() +
  scale_fill_viridis_d() +
  ggtitle("Términos más probables por tema", subtitle = "Modelo LDA, k = 2500") +
  labs(fill = "Tema (k)", x = "Término", y = "β") +
  theme_minimal() +
  theme_beautiful

ggsave("webScrapping/LDA_tesis.png", plot = plotLDA_Tesis, scale = 2,
       width = 25, height = 9, units = "cm", dpi = 350, device = "png")
ggsave("webScrapping/LDA_rubros.png", plot = plotLDA_Rubros, scale = 2,
       width = 25, height = 9, units = "cm", dpi = 350, device = "png")
