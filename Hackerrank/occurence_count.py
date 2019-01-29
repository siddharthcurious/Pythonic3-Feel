def count_topic_occurences(topics, reviews):
    """
    :param topics: A mapping of topic name to topic keyword list.
    :type topics: dict of str -> list
    :param reviews: A list of Yelp reviews.
    :type reviews: list of str
    :return: A mapping of topic name to topic occurences in the given list of reviews.
    :rtype: dict of str -> int
    """
    # TODO: Complete me.
    review_s1 = [ line.replace(".", " ") for line in reviews]
    review_s2 = [ line.replace(",", " ") for line in review_s1]
    review_s3 = " ".join(review_s2)
    review_s3.replace("!", "")
    print(review_s3)
    result = {}
    for key, value in topics.items():
        for v in value:
            pass


if __name__ == "__main__":



    topics = {

    "Price": ["cheap", "expensive", "price"],
    "Business specialties": ["gnome", "gnomes"],
    "Harry Shrub": ["harry shrub"]
}

reviews = [

    "Harry Shrub did a great job with my garden, but I expected more gnomes for the price.",
    "I love my new gnomes, they are so cute! My dog loves them too! Thanks Harry!",
    "Very expensive at fifty dollars per gnome. Next time I'll buy from Cheap Gnomes Warehouse."
]

count_topic_occurences(topics, reviews)