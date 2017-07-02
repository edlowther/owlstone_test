import json

def json_exporter(publishers):
    """Exports data as json to be consumed by the project's web interface.
    
    Args: 
        publishers: A dictionary with publisher names as keys and Publisher objects as values
    """
    data_to_export = []
    for publisher_name, publisher in publishers.items():
        data_to_export.append({
            'publisher_name': publisher_name,
            'average_word_count_by_article': publisher.get_average_word_count_by_article()
        })
    with open('./owlstone_test/owlstone_test/data/publisher_data.json', 'w') as f:
        json.dump(data_to_export, f)