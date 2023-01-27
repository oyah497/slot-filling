import os
from collections import defaultdict


snips_map = {
    # =========================================
    'AddToPlaylist': {
        'domain_desc': 'add to playlist',
        'slot_info': {
            # 'music_item', 'playlist_owner', 'entity_name', 'playlist', 'artist'
            'music_item': {
                'slot_type': 'music_item',
                'slot_desc': 'music item',
                'slot_example': {
                    'context': 'funk outta here please add a piece to my playlist',
                    'true_response': 'piece',
                },
                'my_template': 'the music item is %s.',
                'question': 'what is the music item?',
                'before': 'the music item is ',
                'after': '.'
            },
            'playlist_owner': {
                'slot_type': 'playlist_owner',
                'slot_desc': 'owner',
                'slot_example': {
                    'context': 'add the album to sebastian s ejercicio playlist',
                    'true_response': 'sebastian s',
                },
                'my_template': '%s playlist.',
                'question': 'whose playlist?',
                'before': '',
                'after': ' playlist.'

            },
            'entity_name': {
                'slot_type': 'entity_name',
                'slot_desc': 'entity name',
                'slot_example': {
                    'context': 'i am going to add love letter to my list of parties',
                    'true_response': 'love letter',
                },
                'my_template': 'the song is %s.',
                'question': 'what is the name of the song?',
                'before': 'the song is ',
                'after': '.'
            },
            'playlist': {
                'slot_type': 'playlist',
                'slot_desc': 'playlist',
                'slot_example': {
                    'context': 'add this song to my stay happy playlist',
                    'true_response': 'stay happy',
                },
                'my_template': 'the song is added to %s.',
                'question': 'which playlist is the song added to?',
                'before': 'the song is added to ',
                'after': '.'
            },
            'artist': {
                'slot_type': 'artist',
                'slot_desc': 'artist',
                'slot_example': {
                    'context': 'i am going to include the taylor swift track in my bass gaming playlist',
                    'true_response': 'taylor swift',
                },
                'my_template': 'play something by %s.',
                'question': 'what is the name of the artist?',
                'before': 'play something by ',
                'after': '.'
            },
        }
    },
    # =========================================
    'BookRestaurant': {
        'domain_desc': 'book restaurant',
        'slot_info': {
            # 'city', 'facility', 'timeRange', 'restaurant_name', 'country', 'cuisine', 'restaurant_type',
            #                        'served_dish', 'party_size_number', 'poi', 'sort', 'spatial_relation', 'state',
            #                        'party_size_description'
            'city': {
                'slot_type': 'city',
                'slot_desc': 'city',
                'slot_example': {
                    'context': 'make a reservation at the best pub in shanghai',
                    'true_response': 'shanghai',
                },
                'my_template': 'the city is %s.',
                'question': 'what city?',
                'before': 'the city is ',
                'after': '.'
            },
            'facility': {
                'slot_type': 'facility',
                'slot_desc': 'facility',
                'slot_example': {
                    'context': 'in washington reserve a tavern with baby chair',
                    'true_response': 'baby chair',
                },
                'my_template': 'the restaurant has %s.',
                'question': 'what is the facility?',
                'before': 'the restaurant has ',
                'after': '.'
            },
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_example': {
                    'context': 'i need a reservation for the chinese food in cuba in 10 minutes',
                    'true_response': 'in 10 minutes',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.'
            },
            'restaurant_name': {
                'slot_type': 'restaurant_name',
                'slot_desc': 'restaurant name',
                'slot_example': {
                    'context': 'i am going to kfc together with my friends',
                    'true_response': 'kfc',
                },
                'my_template': 'the restaurant is called %s.',
                'question': 'what is the name of the restaurant?',
                'before': 'the restaurant is called ',
                'after': '.'
                
            },
            'country': {
                'slot_type': 'country',
                'slot_desc': 'country',
                'slot_example': {
                    'context': 'at 9 am reserve a restaurant in jerusalem for 8 persons',
                    'true_response': 'jerusalem',
                },
                'my_template': 'the country is %s.',
                'question': 'what country?',
                'before': 'the country is ',
                'after': '.'
                
            },
            'cuisine': {
                'slot_type': 'cuisine',
                'slot_desc': 'cuisine',
                'slot_example': {
                    'context': 'i d like to reserve a table for one at a spanish restaurant in wesley',
                    'true_response': 'spanish',
                },
                'my_template': 'it is %s cuisine.',
                'question': 'what cuisine is it?',
                'before': 'it is ',
                'after': ' cuisine.'
                
            },
            'restaurant_type': {
                'slot_type': 'restaurant_type',
                'slot_desc': 'restaurant type',
                'slot_example': {
                    'context': 'i d like to reserve a buffet for my family',
                    'true_response': 'buffet',
                },
                'my_template': 'I reserved a %s.',
                'question': 'what kind of eatery is reserved?',
                'before': 'I reserved a ',
                'after': '.'
            },
            'served_dish': {
                'slot_type': 'served_dish',
                'slot_desc': 'served dish',
                'slot_example': {
                    'context': 'find a restaurant serves hot-pot and make a reservation',
                    'true_response': 'hot-pot',
                },
                'my_template': 'the restaurant serves %s.',
                'question': 'what kind of dish does the restaurant serve?',
                'before': 'the restaurant serves ',
                'after': '.'
            },
            'party_size_number': {
                'slot_type': 'party_size_number',
                'slot_desc': 'number of people',
                'slot_example': {
                    'context': 'make a six-person reservation at an alpine wine bar',
                    'true_response': 'six-person',
                },
                'my_template': 'the number is %s.',
                'question': 'What is the number of people at the party?',
                'before': 'the number is ',
                'after': '.'
            },
            'poi': {
                'slot_type': 'poi',
                'slot_desc': 'position',
                'slot_example': {
                    'context': 'i d want to reserve a restaurant near my hotel',
                    'true_response': 'near my hotel',
                },
                'my_template': 'the position is %s.',
                'question': 'where is the restaurant?',
                'before': 'the position is ',
                'after': '.'
            },
            'sort': {
                'slot_type': 'sort',
                'slot_desc': 'type',
                'slot_example': {
                    'context': 'get a highly regarded sandwich shop in colombia',
                    'true_response': 'highly regarded',
                },
                'my_template': 'the restaurant is %s restaurant.',
                'question': 'How is the restaurant s reputation?',
                'before': 'the restaurant is ',
                'after': ' restaurant.'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_example': {
                    'context': 'book a restaurant for 2 that s 10 minutes walk from here',
                    'true_response': '10 minutes walk',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.'
            },
            'state': {
                'slot_type': 'state',
                'slot_desc': 'state',
                'slot_example': {
                    'context': 'we d want to go to a brasserie in omaha that serves sicilian cuisine',
                    'true_response': 'omaha',
                },
                'my_template': 'the state is %s.',
                'question': 'what state?',
                'before': 'the state is ',
                'after': '.'
            },
            'party_size_description': {
                'slot_type': 'party_size_description',
                'slot_desc': 'person',
                'slot_example': {
                    'context': 'book a table for sebastian perez and leclerc',
                    'true_response': 'sebastian perez and leclerc',
                },
                'my_template': 'the restaurant is reserved for %s.',
                'question': 'Who are the people attending the party?',
                'before': 'the restaurant is reserved for ',
                'after': '.'
            },
        }
    },
    # =========================================
    'GetWeather': {
        'domain_desc': 'get weather',
        'slot_info': {
            # 'city', 'state', 'timeRange', 'current_location', 'country', 'spatial_relation', 'geographic_poi',
            #                    'condition_temperature', 'condition_description'
            'city': {
                'slot_type': 'city',
                'slot_desc': 'city',
                'slot_example': {
                    'context': 'is the temperature going down to 2 in shanghai',
                    'true_response': 'shanghai',
                },
                'my_template': 'the city is %s.',
                'question': 'what city?',
                'before': 'the city is ',
                'after': '.'
            },
            'state': {
                'slot_type': 'state',
                'slot_desc': 'state',
                'slot_example': {
                    'context': 'check the weather in omaha',
                    'true_response': 'omaha',
                },
                'my_template': 'the state is %s.',
                'question': 'what state?',
                'before': 'the state is ',
                'after': '.'
            },
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_example': {
                    'context': 'what is the forecast for haidian in next half an hour',
                    'true_response': 'in next half an hour',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.'
            },
            'current_location': {
                'slot_type': 'current_location',
                'slot_desc': 'current location',
                'slot_example': {
                    'context': 'will it rain in my present local street on 11/10/2023',
                    'true_response': 'present local street',
                },
                'my_template': 'the current location is %s.',
                'question': 'where is the current location?',
                'before': 'the current location is ',
                'after': '.'
            },
            'country': {
                'slot_type': 'country',
                'slot_desc': 'country',
                'slot_example': {
                    'context': 'what s the weather like in jerusalem right now',
                    'true_response': 'jerusalem',
                },
                'my_template': 'the country is %s.',
                'question': 'what country?',
                'before': 'the country is ',
                'after': '.'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_example': {
                    'context': 'is it going to rain within 10 minutes bus distance',
                    'true_response': 'within 10 minutes bus distance',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.'
            },
            'geographic_poi': {
                'slot_type': 'geographic_poi',
                'slot_desc': 'geographic position',
                'slot_example': {
                    'context': 'in west lake park, how cold will it be tomorrow',
                    'true_response': 'west lake park',
                },
                'my_template': 'that place is called %s.',
                'question': 'what is the name of the place?',
                'before': 'that place is called ',
                'after': '.'
            },
            'condition_temperature': {
                'slot_type': 'condition_temperature',
                'slot_desc': 'temperature',
                'slot_example': {
                    'context': 'will it get hotter in 2 hours',
                    'true_response': 'hotter',
                },
                'my_template': 'temperatures are %s.',
                'question': 'How are the temperatures?',
                'before': 'temperatures are ',
                'after': '.'
            },
            'condition_description': {
                'slot_type': 'condition_description',
                'slot_desc': 'weather',
                'slot_example': {
                    'context': 'will israel be hit by a snow storm',
                    'true_response': 'snow storm',
                },
                'my_template': 'the weather is %s.',
                'question': 'How is the weather?',
                'before': 'the weather is ',
                'after': '.'
            },
        }
    },
    # =========================================
    'PlayMusic': {
        'domain_desc': 'play music',
        'slot_info': {
            # 'genre', 'music_item', 'service', 'year', 'playlist', 'album', 'sort', 'track', 'artist'
            'genre': {
                'slot_type': 'genre',
                'slot_desc': 'genre',
                'slot_example': {
                    'context': 'find me a lullaby in netease cloud music',
                    'true_response': 'lullaby',
                },
                'my_template': 'I listen to %s.',
                'question': 'what kind of music do yuo listen to?',
                'before': 'I listen to ',
                'after': '.'
            },
            'music_item': {
                'slot_type': 'music_item',
                'slot_desc': 'music item',
                'slot_example': {
                    'context': 'funk outta here please add a piece to my playlist',
                    'true_response': 'piece',
                },
                'my_template': 'the music item is %s.',
                'question': 'what is the music item?',
                'before': 'the music item is ',
                'after': '.'
            },
            'service': {
                'slot_type': 'service',
                'slot_desc': 'service',
                'slot_example': {
                    'context': 'find me a lullaby in netease cloud music',
                    'true_response': 'netease cloud music',
                },
                'my_template': 'play the music on %s.',
                'question': 'what is the name of the service?',
                'before': 'play the music on ',
                'after': '.'
            },
            'year': {
                'slot_type': 'year',
                'slot_desc': 'year',
                'slot_example': {
                    'context': 'play the most popular song in 2021',
                    'true_response': '2021',
                },
                'my_template': 'the year or decade is %s.',
                'question': 'what year or decade is it?',
                'before': 'the year or decade is ',
                'after': '.'
            },
            'playlist': {
                'slot_type': 'playlist',
                'slot_desc': 'playlist',
                'slot_example': {
                    'context': 'add this song to my stay happy playlist',
                    'true_response': 'stay happy',
                },
                'my_template': 'the song is added to %s.',
                'question': 'which playlist is the song added to?',
                'before': 'the song is added to ',
                'after': '.'
            },
            'album': {
                'slot_type': 'album',
                'slot_desc': 'album',
                'slot_example': {
                    'context': 'play the album getting ready by eason chan',
                    'true_response': 'getting ready',
                },
                'my_template': 'play the song from %s.',
                'question': 'what is the name of the album?',
                'before': 'play the song from ',
                'after': '.'
            },
            'sort': {
                'slot_type': 'sort',
                'slot_desc': 'type',
                'slot_example': {
                    'context': 'play the most popular song in 2021',
                    'true_response': 'the most popular',
                },
                'my_template': 'the song is %s song.',
                'question': 'what is that song about?',
                'before': 'the song is ',
                'after': ' song.'
            },
            'track': {
                'slot_type': 'track',
                'slot_desc': 'track',
                'slot_example': {
                    'context': 'play shall we talk by eason chan',
                    'true_response': 'shall we talk',
                },
                'my_template': 'the track is called %s.',
                'question': 'what is the name of the sound track?',
                'before': 'the track is called ',
                'after': '.'
            },
            'artist': {
                'slot_type': 'artist',
                'slot_desc': 'artist',
                'slot_example': {
                    'context': 'i am going to include the taylor swift track in my bass gaming playlist',
                    'true_response': 'taylor swift',
                },
                'my_template': 'play something by %s.',
                'question': 'what is the name of the artist?',
                'before': 'play something by ',
                'after': '.'
            },
        }
    },
    # =========================================
    'RateBook': {
        'domain_desc': 'rate book',
        'slot_info': {
            # 'object_part_of_series_type', 'object_select', 'rating_value', 'object_name', 'object_type',
            #                  'rating_unit', 'best_rating'
            'object_part_of_series_type': {
                'slot_type': 'object_part_of_series_type',
                'slot_desc': 'series',
                'slot_example': {
                    'context': 'i rate the sequel 0 point',
                    'true_response': 'sequel',
                },
                'my_template': 'rate this %s.',
                'question': 'what kind of series is it?',
                'before': 'rate this ',
                'after': '.'
            },
            'object_select': {
                'slot_type': 'object_select',
                'slot_desc': 'this current',
                'slot_example': {
                    'context': 'that book deserves a 5 stars',
                    'true_response': 'that',
                },
                'my_template': 'rate %s book.',
                'question': 'which of the books is rated?',
                'before': 'rate ',
                'after': ' book.'
            },
            'rating_value': {
                'slot_type': 'rating_value',
                'slot_desc': 'rating value',
                'slot_example': {
                    'context': 'the book deserves a 5 stars',
                    'true_response': '5',
                },
                'my_template': 'the book gets %s stars.',
                'question': 'How many points does the book get?',
                'before': 'the book gets ',
                'after': ' stars.'
            },
            'object_name': {
                'slot_type': 'object_name',
                'slot_desc': 'object name',
                'slot_example': {
                    'context': 'i rate lessons from madame chic 10 stars',
                    'true_response': 'lessons from madame chic',
                },
                'my_template': 'the book is called %s.',
                'question': 'what is the name of the rated book?',
                'before': 'the book is called ',
                'after': '.'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_example': {
                    'context': 'this horror literature deserves a 5 stars',
                    'true_response': 'horror',
                },
                'my_template': 'rate this %s.',
                'question': 'what kind of book is it?',
                'before': 'rate this ',
                'after': '.'
            },
            'rating_unit': {
                'slot_type': 'rating_unit',
                'slot_desc': 'rating unit',
                'slot_example': {
                    'context': 'this book deserves a 5 stars',
                    'true_response': 'stars',
                },
                'my_template': 'the book deserves a few %s.',
                'question': 'what are you counting?',
                'before': 'the book deserves a few ',
                'after': '.'
            },
            'best_rating': {
                'slot_type': 'best_rating',
                'slot_desc': 'best rating',
                'slot_example': {
                    'context': 'the highest rating for this book is 10',
                    'true_response': '10',
                },
                'my_template': 'it is %s point rating scale.',
                'question': 'what is the rating scale?',
                'before': 'it is ',
                'after': ' point rating scale.'
            },
        }
    },
    # =========================================
    'SearchCreativeWork': {
        'domain_desc': 'search creative work',
        'slot_info': {
            # 'object_name', 'object_type'
            'object_name': {
                'slot_type': 'object_name',
                'slot_desc': 'object name',
                'slot_example': {
                    'context': 'paris baguette is a bakery chain based in south korea owned by the spc group',
                    'true_response': 'paris baguette',
                },
                'my_template': 'I found %s.',
                'question': 'what are you searching?',
                'before': 'I found ',
                'after': '.'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_example': {
                    'context': 'paris baguette is a bakery chain based in south korea owned by the spc group',
                    'true_response': 'bakery',
                },
                'my_template': 'that %s is great.',
                'question': 'what kind of works are you searching?',
                'before': 'that ',
                'after': ' is great.'
            },
        }
    },
    # =========================================
    'SearchScreeningEvent': {
        'domain_desc': 'search screening event',
        'slot_info': {
            # 'timeRange', 'movie_type', 'object_location_type', 'object_type', 'location_name',
            #                              'spatial_relation', 'movie_name'
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_example': {
                    'context': 'the movie starts at half past eight pm',
                    'true_response': 'half past eight pm',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.'
            },
            'movie_type': {
                'slot_type': 'movie_type',
                'slot_desc': 'movie type',
                'slot_example': {
                    'context': 'i want to see a comedy like green book',
                    'true_response': 'comedy',
                },
                'my_template': 'i am looking for the %s.',
                'question': 'what kind of movies are you looking for?',
                'before': 'i am looking for the ',
                'after': '.'
            },
            'object_location_type': {
                'slot_type': 'object_location_type',
                'slot_desc': 'location type',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'movie house',
                },
                'my_template': 'i will watch the movie at the closest %s.',
                'question': 'what is the location type?',
                'before': 'i will watch the movie at the closest ',
                'after': '.'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_example': {
                    'context': 'show me the movie poster of green book',
                    'true_response': 'movie poster',
                },
                'my_template': 'show %s.',
                'question': 'what are you looking for?',
                'before': 'show ',
                'after': '.'
            },
            'location_name': {
                'slot_type': 'location_name',
                'slot_desc': 'location name',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'the castro theatre',
                },
                'my_template': 'that place is called %s.',
                'question': 'what is the name of the place?',
                'before': 'that place is called ',
                'after': '.'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'closest',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.'
            },
            'movie_name': {
                'slot_type': 'movie_name',
                'slot_desc': 'movie name',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'green book',
                },
                'my_template': 'the movie is called %s.',
                'question': 'what is the name of the movie?',
                'before': 'the movie is called ',
                'after': '.'
            },
        }
    },
}


snips_domains = []
domain2desc = {'atis': 'airline travel'}
domain2slots = {}

domainslot2desc = {}
domainslot2example = {}
domainslot2context = {}

domainslot2temp = {}
domainslot2question = {}
domainslot2before = {}
domainslot2after = {}







for domain_name, domain_item in snips_map.items():
    snips_domains.append(domain_name)
    domain2desc[domain_name] = domain_item['domain_desc']
    domain2slots[domain_name] = list(domain_item['slot_info'].keys())

    domainslot2desc[domain_name] = {}
    domainslot2example[domain_name] = {}
    domainslot2context[domain_name] = {}

    domainslot2temp[domain_name] = {}
    domainslot2question[domain_name] = {}
    domainslot2before[domain_name] = {}
    domainslot2after[domain_name] = {}


    for slot_name, slot_item in domain_item['slot_info'].items():
        domainslot2desc[domain_name][slot_name] = slot_item['slot_desc']
        domainslot2example[domain_name][slot_name] = slot_item['slot_example']['true_response']
        domainslot2context[domain_name][slot_name] = slot_item['slot_example']['context']

        domainslot2temp[domain_name][slot_name] = slot_item['my_template']
        domainslot2question[domain_name][slot_name] = slot_item['question']
        domainslot2before[domain_name][slot_name] = slot_item['before']
        domainslot2after[domain_name][slot_name] = slot_item['after']

domain2slots['atis'] = []
domainslot2desc['atis'] = {}
domainslot2example['atis'] = {}
with open('gsl/datasets/atis_slot_info.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        line_strip = line.strip('\n').split('\t')
        slot = line_strip[0]
        domainslot2desc['atis'][slot] = line_strip[1]
        domain2slots['atis'].append(slot)
        domainslot2example['atis'][slot] = line_strip[2:]


#unseen_slot = {
#    'AddToPlaylist': ['playlist_owner', 'entity_name'] , 
#    'BookRestaurant': ['restaurant_type', 'served_dish', 'restaurant_name', 'party_size_description', 'cuisine', 'party_size_description', ], 
#    'GetWeather': [], 
#    'PlayMusic': [], 
#    'RateBook': [], 
#    'SearchCreativeWork': [], 
#    'SearchScreeningEvent': []
#    }


 # 'music_item', 'playlist_owner', 'entity_name', 'playlist', 'artist'

 # 'city', 'facility', 'timeRange', 'restaurant_name', 'country', 'cuisine', 'restaurant_type',
            #                        'served_dish', 'party_size_number', 'poi', 'sort', 'spatial_relation', 'state',
            #                        'party_size_description'

 # 'city', 'state', 'timeRange', 'current_location', 'country', 'spatial_relation', 'geographic_poi',
            #                    'condition_temperature', 'condition_description'

# 'genre', 'music_item', 'service', 'year', 'playlist', 'album', 'sort', 'track', 'artist'

# 'object_part_of_series_type', 'object_select', 'rating_value', 'object_name', 'object_type',
            #                  'rating_unit', 'best_rating'


# 'timeRange', 'movie_type', 'object_location_type', 'object_type', 'location_name',
            # 












def bio2sl(sentence_bio, domain):
    """
    Args:
        sentence_bio: raw line of file
        domain: domain_name

    Returns:
        [(domain, sentence, entity1, slot1), (domain, sentence, entity2, slot2), ...]
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
        results.append((domain, sentence, entities, slot_type))
    return results


def bio2sl_modified(sentence_bio, domain):
    """
    Args:
        sentence_bio: raw line of file
        domain: domain_name

    Returns:
        [(domain, sentence, entity1, slot1), (domain, sentence, entity2, slot2), ...]
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
    

    for k in snips_map[domain]["slot_info"].keys():
        if (collect_dict.get(k) == None):
#            collect_dict[k].append("")
            collect_dict[k].append("")


    for slot_type, entities in collect_dict.items():
        results.append((domain, sentence, entities, slot_type))

    return results





def load_file(file_path, domain):
    content = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            content.extend(bio2sl_modified(line.strip(), domain))  # domain, sentence, entity list, slot
    return content


def load_snips_data(data_dir):
    domain2data = {}
    for domain in snips_domains:
        file_path = os.path.join(data_dir, 'snips', domain, f'{domain}.txt')
        domain2data[domain] = load_file(file_path, domain)
    return domain2data


def load_snips_seen_unseen_data(data_dir):
    domain2data_seen = {}
    domain2data_unseen = {}
    for domain in snips_domains:
        seen_file_path = os.path.join(data_dir, 'snips', domain, f'seen_slots.txt')
        unseen_file_path = os.path.join(data_dir, 'snips', domain, f'unseen_slots.txt')
        domain2data_seen[domain] = load_file(seen_file_path, domain)
        domain2data_unseen[domain] = load_file(unseen_file_path, domain)
    return domain2data_seen, domain2data_unseen


def load_atis_data(data_dir):
    file_path = os.path.join(data_dir, 'atis', 'atis.txt')

    return {'atis' : []}
    return {'atis': load_file(file_path, 'atis')}
#    intents = ['atis_airfare', 'atis_airline', 'atis_flight', 'atis_ground_service', 'others']
#    content = []

#    for intent in intents:
#        intent_path = os.path.join(data_dir, 'atis', intent, f'{intent}.txt')
#        content.extend(load_file(intent_path, 'atis'))

#    return {'atis': content}

#    airfare_path = os.path.join(data_dir, 'atis', 'atis_airfare', 'atis_airfare.txt')
#    content = load_file(airfare_path, 'atis')





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


    valid_num = len(all_data[target_domain]) // 10
    train_data.extend(all_data[target_domain][:shot_num])  # [(domain, sentence, entity list, slot), ...]
    valid_data.extend(all_data[target_domain][shot_num:(valid_num + shot_num)])
    test_data.extend(all_data[target_domain][(valid_num + shot_num):])
    #test_data.extend(all_data[target_domain][500:700])

    if target_domain != 'atis':
        domain2data_seen, domain2data_unseen = load_snips_seen_unseen_data(data_dir)
        seen_data = domain2data_seen[target_domain]
        unseen_data = domain2data_unseen[target_domain]
        return train_data, valid_data, test_data, seen_data, unseen_data

    return train_data, valid_data, test_data, None, None


def slot_list(data):
    sl = []

    for domain, sentence, entity, slot in data:
        sl.append(slot)
    
    return sl