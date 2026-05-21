from google.cloud import bigquery

from src.utils.logger import setup_logger

logger = setup_logger()


def create_monthly_sales():

    client = bigquery.Client()

    logger.info(
        "Creating monthly sales KPI table"
    )

    query = """

    CREATE OR REPLACE TABLE
    `food-sales-analytics-prod.food_sales.gold_monthly_sales`
    AS

    SELECT

        EXTRACT(YEAR FROM orderDate) AS year,

        EXTRACT(MONTH FROM orderDate) AS month,

        COUNT(order_id) AS total_orders,

        SUM(quantity) AS total_quantity

    FROM
    `food-sales-analytics-prod.food_sales.silver_orders`

    GROUP BY
    year,
    month

    ORDER BY
    year,
    month

    """

    job = client.query(query)

    job.result()

    logger.info(
        "gold_monthly_sales created"
    )


def create_payment_analysis():

    client = bigquery.Client()

    logger.info(
        "Creating payment analysis table"
    )

    query = """

    CREATE OR REPLACE TABLE
    `food-sales-analytics-prod.food_sales.gold_payment_analysis`
    AS

    SELECT

        payment_method,

        COUNT(order_id) AS total_orders,

        SUM(quantity) AS total_quantity

    FROM
    `food-sales-analytics-prod.food_sales.silver_orders`

    GROUP BY
    payment_method

    """

    job = client.query(query)

    job.result()

    logger.info(
        "gold_payment_analysis created"
    )


def create_restaurant_performance():

    client = bigquery.Client()

    logger.info(
        "Creating restaurant performance table"
    )

    query = """

    CREATE OR REPLACE TABLE
    `food-sales-analytics-prod.food_sales.gold_restaurant_performance`
    AS

    SELECT

        Resturant_ID,

        COUNT(order_id) AS total_orders,

        SUM(quantity) AS total_quantity

    FROM
    `food-sales-analytics-prod.food_sales.silver_orders`

    GROUP BY
    Resturant_ID

    ORDER BY
    total_orders DESC

    """

    job = client.query(query)

    job.result()

    logger.info(
        "gold_restaurant_performance created"
    )


def create_delivery_analysis():

    client = bigquery.Client()

    logger.info(
        "Creating delivery analysis table"
    )

    query = """

    CREATE OR REPLACE TABLE
    `food-sales-analytics-prod.food_sales.gold_delivery_analysis`
    AS

    SELECT

        deliver_status,

        COUNT(order_id) AS total_orders

    FROM
    `food-sales-analytics-prod.food_sales.silver_orders`

    GROUP BY
    deliver_status

    """

    job = client.query(query)

    job.result()

    logger.info(
        "gold_delivery_analysis created"
    )


def load_gold_layer():

    logger.info(
        "Gold layer processing started"
    )

    create_monthly_sales()

    create_payment_analysis()

    create_restaurant_performance()

    create_delivery_analysis()

    logger.info(
        "Gold layer processing completed"
    )