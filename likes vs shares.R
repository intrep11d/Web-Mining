# set up
require(ggplot2)
require(dplyr)
library(scales)

library("showtext")
font_add_google("Roboto", "roboto")
font_add_google("Playfair Display", "playfair")
font_add_google("Lato", "lato")
showtext_auto()

all_user_videos <- read.csv("~/Downloads/SOC NUS Web Mining/all_user_videos.csv")
tiktok_videos <- read.csv("~/Downloads/SOC NUS Web Mining/tiktok_videos.csv")
tiktok_videos$video_length <- NULL

videos <- rbind(all_user_videos, tiktok_videos)
videos$is_original <- grepl("original", videos$music_title, ignore.case = TRUE)

# data management
videos_binned <- videos %>%
  mutate(
    likes_bin = cut(
      likes,
      breaks = c(-Inf, 100, 500, 1000, 5000, 10000, 100000, 500000, Inf),
      labels = c("<100", "100–499", "500–999", "1000–4999", "5000–9999", "10000–99999", "100000–499999", "500000+"),
      right = FALSE
    ),
    shares_bin = cut(
      shares,
      breaks = c(-Inf, 10, 50, 100, 500, 1000, 5000, 10000, Inf),
      labels = c("<10", "10–49", "50–99", "100–499", "500–999", "1000–4999", "5000–9999", "10000+"),
      right = FALSE
    )
  )

videos_original <- videos_binned %>% filter(is_original)
videos_not_original <- videos_binned %>% filter(!is_original)

heatmap_original <- videos_original %>%
  group_by(likes_bin, shares_bin) %>%
  summarise(count = n(), .groups = "drop") %>%
  mutate(log_count = log10(count + 1))

heatmap_not_original <- videos_not_original %>%
  group_by(likes_bin, shares_bin) %>%
  summarise(count = n(), .groups = "drop") %>%
  mutate(log_count = log10(count + 1))

# plots
ggplot(heatmap_original, aes(x = likes_bin, y = shares_bin, fill = log_count)) +
  geom_tile(color = "white") +
  scale_fill_viridis_c(
    option = "plasma",
    na.value = "grey90",
    breaks = log10(c(1, 10, 100, 1000, 10000) + 1),
    labels = c("1", "10", "100", "1000", "10000+")
  ) +
  labs(
    x = "Likes",
    y = "Shares",
    fill = "Count",
    title = "No. of Videos by Likes and Shares",
    subtitle = "VIDEOS WITH ORIGINAL AUDIO"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, size = 8, margin = margin(t = 5), family = "roboto"),
    axis.text.y = element_text(size = 8, margin = margin(r = 5), family = "roboto"),
    axis.title.x = element_text(size = 12, margin = margin(t = -20), family = "roboto"),
    axis.title.y = element_text(size = 12, margin = margin(r = -12), family = "roboto"),
    plot.background = element_rect(fill = "#f5faf2", color = NA),
    plot.title.position = "plot",
    plot.title = element_text(family = "playfair", size = 18, face = "bold", margin = margin(0, 0, 5, 0)),
    plot.subtitle = element_text(family = "lato", size = 10, margin = margin(0, 0, 13, 2)),
    legend.text = element_text(family = "roboto", size = 7),
    legend.title = element_text(family = "roboto", size = 8, face = "bold"),
    legend.justification = "right",
    legend.direction = "vertical",
    legend.key.size = unit(0.3, "cm"),
    legend.box.margin = margin(5, 0, 10, 1),
    strip.text = element_text(family = "roboto", size = 9)
  )


ggplot(heatmap_not_original, aes(x = likes_bin, y = shares_bin, fill = log_count)) +
  geom_tile(color = "white") +
  scale_fill_viridis_c(
    option = "plasma",
    na.value = "grey90",
    breaks = log10(c(1, 10, 100, 1000, 10000) + 1),
    labels = c("1", "10", "100", "1000", "10000+")
  ) +
  labs(
    x = "Likes",
    y = "Shares",
    fill = "Count",
    title = "No. of Videos by Likes and Shares",
    subtitle = "VIDEOS WITH NON-ORIGINAL AUDIO"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, size = 8, margin = margin(t = 5), family = "roboto"),
    axis.text.y = element_text(size = 8, margin = margin(r = 5), family = "roboto"),
    axis.title.x = element_text(size = 12, margin = margin(t = -20), family = "roboto"),
    axis.title.y = element_text(size = 12, margin = margin(r = -12), family = "roboto"),
    plot.background = element_rect(fill = "#f5faf2", color = NA),
    plot.title.position = "plot",
    plot.title = element_text(family = "playfair", size = 18, face = "bold", margin = margin(0, 0, 5, 0)),
    plot.subtitle = element_text(family = "lato", size = 10, margin = margin(0, 0, 13, 2)),
    legend.text = element_text(family = "roboto", size = 7),
    legend.title = element_text(family = "roboto", size = 8, face = "bold"),
    legend.justification = "right",
    legend.direction = "vertical",
    legend.key.size = unit(0.3, "cm"),
    legend.box.margin = margin(5, 0, 10, 1),
    strip.text = element_text(family = "roboto", size = 9)
  )


