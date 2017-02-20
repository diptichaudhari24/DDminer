# load required libraries
suppressMessages(library(rpart))
suppressMessages(library(rattle))

# read command line arguments
args <- commandArgs(trailingOnly = TRUE)
grid_number <- args[1]
age <- as.numeric(args[2])
sex <- args[3]

# read dataset
data_directory <- "/home/dipti/Desktop/ddminer_datasets/"
filename <- paste0("ddminer_dataset_grid_", grid_number, ".csv")
ddminer_dataset <- read.csv(paste0(data_directory, filename))
ddminer_dataset$survived <- as.factor(ifelse(ddminer_dataset$survived == 1, "YES", "NO"))

# build tree
tree_model <- rpart(survived ~ .,
                    data=ddminer_dataset,
                    method="class")

# plot tree and save to file
png(filename = paste0(data_directory, "tree_plot_grid_", grid_number, ".png"))
fancyRpartPlot(model = tree_model)
invisible(dev.off())

# predict on test point and write to stdout stream
test_point <- data.frame("age"=age, "sex"=sex, "survived"="NO")
test_point_prediction <- as.character(predict(tree_model, newdata=test_point, type="class"))
cat(test_point_prediction)
