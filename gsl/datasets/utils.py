import os
from collections import defaultdict

snips_domains = ['AddToPlaylist', 'BookRestaurant', 'GetWeather', 'PlayMusic', 'RateBook', 'SearchCreativeWork',
                 'SearchScreeningEvent']

domain2slots = {
    "AddToPlaylist": ['music_item', 'playlist_owner', 'entity_name', 'playlist', 'artist'],
    "BookRestaurant": ['city', 'facility', 'timeRange', 'restaurant_name', 'country', 'cuisine', 'restaurant_type',
                       'served_dish', 'party_size_number', 'poi', 'sort', 'spatial_relation', 'state',
                       'party_size_description'],
    "GetWeather": ['city', 'state', 'timeRange', 'current_location', 'country', 'spatial_relation', 'geographic_poi',
                   'condition_temperature', 'condition_description'],
    "PlayMusic": ['genre', 'music_item', 'service', 'year', 'playlist', 'album', 'sort', 'track', 'artist'],
    "RateBook": ['object_part_of_series_type', 'object_select', 'rating_value', 'object_name', 'object_type',
                 'rating_unit', 'best_rating'],
    "SearchCreativeWork": ['object_name', 'object_type'],
    "SearchScreeningEvent": ['timeRange', 'movie_type', 'object_location_type', 'object_type', 'location_name',
                             'spatial_relation', 'movie_name']
}
domain2description = {"AddToPlaylist": "add to playlist", "BookRestaurant": "reserve restaurant",
                      "GetWeather": "get weather",
                      "PlayMusic": "play music", "RateBook": "rate book", "SearchCreativeWork": "search creative work",
                      "SearchScreeningEvent": "search screening event"}
slot2description = {'playlist': 'playlist', 'music_item': 'music item', 'geographic_poi': 'geographic position',
                    'facility': 'facility', 'movie_name': 'movie name', 'location_name': 'location name',
                    'restaurant_name': 'restaurant name', 'track': 'track', 'restaurant_type': 'restaurant type',
                    'object_part_of_series_type': 'series', 'country': 'country', 'service': 'service',
                    'poi': 'position',
                    'party_size_description': 'person', 'served_dish': 'served dish', 'genre': 'genre',
                    'current_location': 'current location', 'object_select': 'this current', 'album': 'album',
                    'object_name': 'object name', 'state': 'location', 'sort': 'type',
                    'object_location_type': 'location type',
                    'movie_type': 'movie type', 'spatial_relation': 'spatial relation', 'artist': 'artist',
                    'cuisine': 'cuisine', 'entity_name': 'entity name', 'object_type': 'object type',
                    'playlist_owner': 'playlist owner', 'timeRange': 'time range', 'city': 'city',
                    'rating_value': 'rating value',
                    'best_rating': 'best rating', 'rating_unit': 'rating unit', 'year': 'year',
                    'party_size_number': 'number',
                    'condition_description': 'weather', 'condition_temperature': 'temperature'}

# use two examples
# slot2example = {
#     # AddToPlaylist
#     "music_item": ["song", "track"],
#     "playlist_owner": ["my", "donna s"],
#     "entity_name": ["the crabfish", "natasha"],
#     "playlist": ["quiero playlist", "workday lounge"],
#     "artist": ["lady bunny", "lisa dalbello"],
#     # BookRestaurant
#     "city": ["north lima", "falmouth"],
#     "facility": ["smoking room", "indoor"],
#     "timeRange": ["9 am", "january the twentieth"],
#     "restaurant_name": ["the maisonette", "robinson house"],
#     "country": ["dominican republic", "togo"],
#     "cuisine": ["ouzeri", "jewish"],
#     "restaurant_type": ["tea house", "tavern"],
#     "served_dish": ["wings", "cheese fries"],
#     "party_size_number": ["seven", "one"],
#     "poi": ["east brady", "fairview"],
#     "sort": ["top-rated", "highly rated"],
#     "spatial_relation": ["close", "faraway"],
#     "state": ["sc", "ut"],
#     "party_size_description": ["me and angeline", "my colleague and i"],
#     # GetWeather
#     "current_location": ["current spot", "here"],
#     "geographic_poi": ["bashkirsky nature reserve", "narew national park"],
#     "condition_temperature": ["chillier", "hot"],
#     "condition_description": ["humidity", "depression"],
#     # PlayMusic
#     "genre": ["techno", "pop"],
#     "service": ["spotify", "groove shark"],
#     "year": ["2005", "1993"],
#     "album": ["allergic", "secrets on parade"],
#     "track": ["in your eyes", "the wizard and i"],
#     # RateBook
#     "object_part_of_series_type": ["series", "saga"],
#     "object_select": ["this", "current"],
#     "rating_value": ["1", "four"],
#     "object_name": ["american tabloid", "my beloved world"],
#     "object_type": ["book", "novel"],
#     "rating_unit": ["points", "stars"],
#     "best_rating": ["6", "5"],
#     # SearchCreativeWork
#     # SearchScreeningEvent
#     "movie_type": ["animated movies", "films"],
#     "object_location_type": ["movie theatre", "cinema"],
#     "location_name": ["amc theaters", "wanda group"],
#     "movie_name": ["on the beat", "for lovers only"]
# }

# new example!!
slot2example = {
    # AddToPlaylist
    "music_item": ["record", "melody"],
    "playlist_owner": ["your", "mom s"],
    "entity_name": ["rain on me", "blinding lights"],
    "playlist": ["watermelon sugar", "dance monkey"],
    "artist": ["lady gaga", "ariana grande"],
    # BookRestaurant
    "city": ["los angeles", "new york"],
    "facility": ["rest room", "outdoor"],
    "timeRange": ["8 pm", "november 29"],
    "restaurant_name": ["mama s fish house", "snow s bbq"],
    "country": ["america", "britain"],
    "cuisine": ["japanese cuisine", "chinese food"],
    "restaurant_type": ["buffet", "pub"],
    "served_dish": ["sushi", "steak"],
    "party_size_number": ["seven", "one"],
    "poi": ["parker pennsylvania", "bailey drive"],
    "sort": ["high class", "top ranking"],
    "spatial_relation": ["remote", "nearby"],
    "state": ["ny", "fl"],
    "party_size_description": ["me and my friend", "my mom and i"],
    # GetWeather
    "current_location": ["my location", "here"],
    "geographic_poi": ["yellowstone national park", "the great wall"],
    "condition_temperature": ["cold", "warm"],
    "condition_description": ["temperature", "atmospheric pressure"],
    # PlayMusic
    "genre": ["classical", "rock"],
    "service": ["pandora", "deezer"],
    "year": ["2022", "2021"],
    "album": ["folklore", "reputation"],
    "track": ["end game", "getaway car"],
    # RateBook
    "object_part_of_series_type": ["series", "saga"],
    "object_select": ["this", "current"],
    "rating_value": ["5", "four"],
    "object_name": ["lessons from madame chic", "how to trade in stocks"],
    "object_type": ["comic book", "fiction"],
    "rating_unit": ["points", "stars"],
    "best_rating": ["6", "5"],
    # SearchCreativeWork
    # SearchScreeningEvent
    "movie_type": ["science fiction films", "comedy"],
    "object_location_type": ["movie theatre", "cinema"],
    "location_name": ["the castro theatre", "film forum"],
    "movie_name": ["titanic", "green book"]
}

domain2slots['atis'] = []
with open('gsl/datasets/atis_slot_info.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        line_strip = line.strip('\n').split('\t')
        slot = line_strip[0]
        slot2description[slot] = line_strip[1]
        domain2slots['atis'].append(slot)
        slot2example[slot] = line_strip[2:]


def bio2sl(sentence_bio):
    """
    Args:
        sentence_bio: raw line of file

    Returns:
        [(sentence, entity1, slot1), (sentence, entity2, slot2), ...]
    """
    sentence, bio = sentence_bio.split('\t')
    char_label_list = list(zip(sentence.split(), bio.split()))

    length = len(char_label_list)
    idx = 0
    entities, slot_types = [], []
    while idx < length:
        char, label = char_label_list[idx]
        label_first_char = label[0]

        # merge chars
        if label_first_char == "O":
            idx += 1
            continue
        if label_first_char == "B":
            end = idx + 1
            while end < length and char_label_list[end][1][0] == "I":
                end += 1
            entity = ' '.join(char_label_list[i][0] for i in range(idx, end))
            entities.append(entity)
            slot_type = label[2:]
            slot_types.append(slot_type)
            idx = end
        else:
            raise Exception('Invalid Inputs: %s' % (char_label_list[idx]))

    # one slot map to one response
    # if one slot has multi entities, only return one result
    results = []
    collect_dict = defaultdict(list)
    for entity, slot_type in zip(entities, slot_types):
        collect_dict[slot_type].append(entity)
    for slot_type, entities in collect_dict.items():
        results.append((sentence, entities, slot_type))
    return results


def load_file(file_path):
    content = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            content.extend(bio2sl(line.strip()))  # sentence, entity list, slot
    return content


def load_snips_data(data_dir):
    domain2data = {}
    for domain in snips_domains:
        file_path = os.path.join(data_dir, 'snips', domain, f'{domain}.txt')
        domain2data[domain] = load_file(file_path)
    return domain2data


def load_snips_seen_unseen_data(data_dir):
    domain2data_seen = {}
    domain2data_unseen = {}
    for domain in snips_domains:
        seen_file_path = os.path.join(data_dir, 'snips', domain, f'seen_slots.txt')
        unseen_file_path = os.path.join(data_dir, 'snips', domain, f'unseen_slots.txt')
        domain2data_seen[domain] = load_file(seen_file_path)
        domain2data_unseen[domain] = load_file(unseen_file_path)
    return domain2data_seen, domain2data_unseen


def load_atis_data(data_dir):
    file_path = os.path.join(data_dir, 'atis', 'atis.txt')
    return {'atis': load_file(file_path)}


def generate_text_data(data_dir, target_domain, shot_num=0):
    snips_data = load_snips_data(data_dir)
    atis_data = load_atis_data(data_dir)
    all_data = {**snips_data, **atis_data}

    train_data = []
    valid_data = []
    test_data = []
    for domain_name, domain_data in all_data.items():
        if domain_name != target_domain and domain_name != 'atis':
            train_data.extend(domain_data)

    train_data.extend(all_data[target_domain][:shot_num])  # [(sentence, entity list, slot), ...]
    valid_data.extend(all_data[target_domain][shot_num:500])
    test_data.extend(all_data[target_domain][500:])

    if target_domain != 'atis':
        domain2data_seen, domain2data_unseen = load_snips_seen_unseen_data(data_dir)
        seen_data = domain2data_seen[target_domain]
        unseen_data = domain2data_unseen[target_domain]
        return train_data, valid_data, test_data, seen_data, unseen_data

    return train_data, valid_data, test_data, None, None
