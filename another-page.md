<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Model Analysis</title>
    <style>
        body {
            font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
            margin: 1in;
        }
        h2 {
            color: #333;
            margin-top: 1em;
        }
        p, ul {
            font-size: 16px;
            line-height: 1.6;
            color: #555;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .section-title {
            font-weight: bold;
            font-size: 18px;
            color: #333;
            margin-top: 1em;
        }
    </style>
</head>
<body>

    <h2>Visualization and Quantitative Scoring Metrics</h2>
    <p>
        The first model we chose to implement was the linear regression model. The visualization created from this implementation was a scatter plot, which showcases the relationship between time elapsed (independent variable) to the power load in MW (dependent variable). The points on the scatterplot represent the preprocessed data of 14 years worth of hourly measurements in the Eastern Interconnection grid. The green linear regression fit line is seen as having a slight negative linear progression. As described in our code, we calculated the correlation coefficient, which is also displayed on our visual as -0.18. This statistic suggests that the relationship between power load and time elapsed is a negative weak correlation.
    </p>

    <div class="section-title">Interpretation</div>
    <p><strong>Correlation:</strong> -0.18 as the correlation coefficient suggests a weak negative relationship between the two variables, time and power load. This means that there is no strong evidence to imply that over time there was a slight decrease in power load in the duration of the 14 years.</p>
    <p><strong>Regression Line:</strong> Looking at the scatterplot as a whole, there is a high level of variance amongst the points over the 14 year period. Because of this high level of variance, the slight decrease from the relationship of these two variables might not be a strong indicator of the true change over time.</p>

    <div class="section-title">Model Performance</div>
    <p>
        Our linear regression model did not give us a strong indicator of the relationship between time and power load. Due to a relatively small correlation coefficient value and almost flat trend line, we could not observe significant patterns to identify due to some of the potential factors listed below.
    </p>
    <ul>
        <li><strong>One Feature:</strong> As we were not able to conclude a significant trend, it is clear that time alone is insufficient as a predictor. As suggested in our proposal, we need to look at other variables, such as weather conditions, day of the week, and geographical location. These other potential features might have a stronger correlation to power load.</li>
        <li><strong>High Variability:</strong> The scatterplot describes a high variability in power load throughout the years. We would need to try incorporating other features, which could indicate why there is such a high level of variability and what features could reduce this.</li>
        <li><strong>Seasonal Patterns:</strong> A linear regression model may not be able to effectively capture cyclical patterns, which may be what is happening with the power load trends on an annual basis. Exploring other modeling options, such as a time-series model with seasonal decomposition could perform better.</li>
    </ul>

    <div class="section-title">Next Steps</div>
    <p>
        For future iterations of our project, we came up with a list of potential improvements we can make to our models and factors to consider for other models we will work on for this project. Based on our analysis of the linear regression model, we came up with these next steps:
    </p>
    <ul>
        <li><strong>Additional Features:</strong> Incorporate other features such as temperature, day of the week, and geographical location to capture more complex relationships.</li>
        <li><strong>Explore Alternatives:</strong> Explore other ML models that may more effectively interpret the data we want to learn about. Some suggestions can include: Random Forests, which can capture non-linear relationships, or time-series models that can account for seasons.</li>
        <li><strong>Other Metrics:</strong> Calculate metrics such as Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE) to quantify the prediction error more accurately.</li>
    </ul>

</body>
</html>
