## A small demo to Extract Books data from multiple categories from Bookstoscrape.com, then store it in Neo4j for better Recommendations. 

This is the base code of a small demo built for the webinar Graphversation Ep. 3 - How Web Scraping and Graph Databases Power Recommendation Engines - https://www.youtube.com/watch?v=Smwr1U1xUQs


### How to run this code
- Follow the guidelines on this [Scrapy tutorial ](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- If you plan to scrape other websites and target large-scale book data extraction. I recommend using Zyte API along with the Scrapy using [scrapy-zyte-api SDk](https://github.com/scrapy-plugins/scrapy-zyte-api) and following this detailed- [Web scraping tutorial](https://docs.zyte.com/web-scraping/tutorial/index.html#tutorial).


### Recommendation Engine 
I followed the Neo4j tutorials to build a basic recommendation engine. Here's the reference I followed [Tutorial: Build a Cypher Recommendation Engine](https://neo4j.com/developer/cypher/guide-build-a-recommendation-engine/) 

#### Steps 
- I created the extracted Books Nodes and People Nodes.
![graph.png](https://github.com/NehaSetiaNagpal/Bookstoscrape.com/blob/main/images/graph.png)


- Then, I created the relationships between them on the basis of their journeys or curated paths to achieve the self-awareness goals of an individual. 
![Screenshot 2023-06-12 at 2.32.28 PM.png](https://github.com/NehaSetiaNagpal/Bookstoscrape.com/blob/main/images/Screenshot%202023-06-12%20at%202.32.28%20PM.png)


- Query for recommending the most chosen path by the users on their self-awareness journey.

 
