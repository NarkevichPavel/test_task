import json
from bs4 import BeautifulSoup
import requests


class States:

    def __init__(self):
        self.url = 'https://dentalia.com/'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }

    def get_states(self):
        scl = requests.get(url=self.url, headers=self.headers)

        req = scl.text

        soup = BeautifulSoup(req, 'lxml')

        html_class = 'jet-listing-grid__items grid-col-desk-1 grid-col-tablet-1 grid-col-mobile-1 jet-listing-grid--231'

        states = soup.find(class_=html_class).find_parent().next_element

        id_states = []

        for state in states:
            data = state.get('data-post-id')
            id_states.append(data)

        return id_states


class Ajax(States):

    def __init__(self):
        super().__init__()
        self.ajax_cookies = {
            '_ga': 'GA1.1.1855238770.1711649654',
            '_gcl_au': '1.1.1396684735.1711649664',
            '_hjSessionUser_3724640': 'eyJpZCI6IjJmYzM1MjliLTE1ZDctNTcwNS04ZmQyLTI1YzkxOThhM2UzMSIsImNyZWF0ZWQiOjE3MTE2NDk2NjQ4MzksImV4aXN0aW5nIjp0cnVlfQ==',
            'PHPSESSID': 'sp6fiv0sfbqkef8e4i6pd231fl',
            '_hjSession_3724640': 'eyJpZCI6ImYxMDA0ZGFiLTk0NzMtNGQyYi1hMjIzLTYzY2ZkYzcxMDk0YSIsImMiOjE3MTE3OTU1MjcxNTMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
            '_ga_EN8BN980LH': 'GS1.1.1711795526.6.1.1711798122.47.0.0',
            '_ga_FMK4KRGVF2': 'GS1.1.1711795526.6.1.1711798122.0.0.0',
            '_ga_94GCJ4Q0CE': 'GS1.1.1711795526.6.1.1711798122.0.0.0',
        }
        self.ajax_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': '_ga=GA1.1.1855238770.1711649654; _gcl_au=1.1.1396684735.1711649664; _hjSessionUser_3724640=eyJpZCI6IjJmYzM1MjliLTE1ZDctNTcwNS04ZmQyLTI1YzkxOThhM2UzMSIsImNyZWF0ZWQiOjE3MTE2NDk2NjQ4MzksImV4aXN0aW5nIjp0cnVlfQ==; PHPSESSID=sp6fiv0sfbqkef8e4i6pd231fl; _hjSession_3724640=eyJpZCI6ImYxMDA0ZGFiLTk0NzMtNGQyYi1hMjIzLTYzY2ZkYzcxMDk0YSIsImMiOjE3MTE3OTU1MjcxNTMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga_EN8BN980LH=GS1.1.1711795526.6.1.1711798122.47.0.0; _ga_FMK4KRGVF2=GS1.1.1711795526.6.1.1711798122.0.0.0; _ga_94GCJ4Q0CE=GS1.1.1711795526.6.1.1711798122.0.0.0',
            'Origin': 'https://dentalia.com',
            'Referer': 'https://dentalia.com/clinica/?jsf=jet-engine:clinicas-archive&tax=estados:19',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.ajax_data = {
            'action': 'jet_smart_filters',
            'provider': 'jet-engine-maps/map',
            'query[_tax_query_estados]': None,
            'defaults[post_status]': 'publish',
            'defaults[post_type]': 'clinicas',
            'defaults[posts_per_page]': '100',
            'defaults[paged]': '1',
            'defaults[ignore_sticky_posts]': '1',
            'settings[lisitng_id]': '6640',
            'settings[address_field]': 'direccion',
            'settings[add_lat_lng]': '',
            'settings[lat_lng_address_field]': '',
            'settings[posts_num]': '100',
            'settings[auto_center]': 'yes',
            'settings[max_zoom]': '15',
            'settings[custom_center]': '',
            'settings[custom_zoom]': '11',
            'settings[zoom_control]': 'auto',
            'settings[zoom_controls]': 'true',
            'settings[fullscreen_control]': 'true',
            'settings[street_view_controls]': 'true',
            'settings[map_type_controls]': '',
            'settings[posts_query][0][_id]': '593cb36',
            'settings[posts_query][0][tax_query_taxonomy]': 'estados',
            'settings[posts_query][0][tax_query_terms]': '%current_terms|estados%{"context":"default_object"}',
            'settings[meta_query_relation]': 'AND',
            'settings[tax_query_relation]': 'AND',
            'settings[hide_widget_if]': '',
            'settings[popup_width]': '450',
            'settings[popup_offset]': '40',
            'settings[marker_type]': 'icon',
            'settings[marker_image][url]': '',
            'settings[marker_image][id]': '',
            'settings[marker_image][size]': '',
            'settings[marker_icon][value]': 'fas fa-map-marker-alt',
            'settings[marker_icon][library]': 'fa-solid',
            'settings[marker_label_type]': 'post_title',
            'settings[marker_label_field]': '',
            'settings[marker_label_field_custom]': '',
            'settings[marker_label_text]': '',
            'settings[marker_label_format_cb]': '0',
            'settings[marker_label_custom]': '',
            'settings[marker_label_custom_output]': '%s',
            'settings[marker_image_field]': '',
            'settings[marker_image_field_custom]': '',
            'settings[multiple_marker_types]': '',
            'settings[marker_clustering]': 'true',
            'settings[popup_pin]': '',
            'settings[popup_preloader]': '',
            'settings[custom_query]': '',
            'settings[custom_query_id]': '10',
            'settings[labels_by_glossary]': '',
            'settings[date_format]': 'F j, Y',
            'settings[num_dec_point]': '.',
            'settings[num_thousands_sep]': ',',
            'settings[human_time_diff_from_key]': '',
            'settings[num_decimals]': '2',
            'settings[zeroise_threshold]': '3',
            'settings[proportion_divisor]': '10',
            'settings[proportion_multiplier]': '5',
            'settings[proportion_precision]': '0',
            'settings[child_path]': '',
            'settings[attachment_image_size]': 'full',
            'settings[thumbnail_add_permalink]': '',
            'settings[related_list_is_single]': '',
            'settings[related_list_is_linked]': 'yes',
            'settings[related_list_tag]': 'ul',
            'settings[multiselect_delimiter]': ', ',
            'settings[switcher_true]': '',
            'settings[switcher_false]': '',
            'settings[url_scheme]': '',
            'settings[checklist_cols_num]': '1',
            'settings[checklist_divider]': '',
            'settings[user_data_to_get]': 'display_name',
            'props[found_posts]': '63',
            'props[max_num_pages]': '1',
            'props[page]': '1',
        }
        self.cookies = {
            '_ga': 'GA1.1.872356557.1711740943',
            '_gcl_au': '1.1.624670784.1711740946',
            '_hjSessionUser_3724640': 'eyJpZCI6ImIyYmI2ODcyLThlNGEtNTI4NS1iYzRmLWUzMzM1ODIxNjE0MiIsImNyZWF0ZWQiOjE3MTE3NDA5NDg1MTAsImV4aXN0aW5nIjp0cnVlfQ==',
            'PHPSESSID': 'oc8hviajco4v8u43ncr7ggipjp',
            '_hjSession_3724640': 'eyJpZCI6IjNiNTZlNzZmLTQ1MjEtNDU1Mi04YzYzLTg1ODI2NWNkMWYwMiIsImMiOjE3MTE3OTE2NDk0MjksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
            '_ga_EN8BN980LH': 'GS1.1.1711799573.4.1.1711800572.59.0.0',
            '_ga_FMK4KRGVF2': 'GS1.1.1711799574.4.1.1711800573.0.0.0',
            '_ga_94GCJ4Q0CE': 'GS1.1.1711799574.4.1.1711800573.0.0.0',
        }
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': '_ga=GA1.1.872356557.1711740943; _gcl_au=1.1.624670784.1711740946; _hjSessionUser_3724640=eyJpZCI6ImIyYmI2ODcyLThlNGEtNTI4NS1iYzRmLWUzMzM1ODIxNjE0MiIsImNyZWF0ZWQiOjE3MTE3NDA5NDg1MTAsImV4aXN0aW5nIjp0cnVlfQ==; PHPSESSID=oc8hviajco4v8u43ncr7ggipjp; _hjSession_3724640=eyJpZCI6IjNiNTZlNzZmLTQ1MjEtNDU1Mi04YzYzLTg1ODI2NWNkMWYwMiIsImMiOjE3MTE3OTE2NDk0MjksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga_EN8BN980LH=GS1.1.1711799573.4.1.1711800572.59.0.0; _ga_FMK4KRGVF2=GS1.1.1711799574.4.1.1711800573.0.0.0; _ga_94GCJ4Q0CE=GS1.1.1711799574.4.1.1711800573.0.0.0',
            'Origin': 'https://dentalia.com',
            'Referer': 'https://dentalia.com/clinica/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.params = {
            'nocache': '1711800575',
        }
        self.data = {
            'action': 'jet_engine_ajax',
            'handler': 'get_listing',
            'page_settings[post_id]': '5883',
            'page_settings[queried_id]': '344706|WP_Post',
            'page_settings[element_id]': 'c1b6043',
            'page_settings[page]': '1',
            'listing_type': 'elementor',
            'isEditMode': 'false',
        }

    def get_ajax_data(self):
        states = self.get_states()
        url = 'https://dentalia.com/wp-admin/admin-ajax.php'

        ajax_data = []

        for state in states:
            self.ajax_data['query[_tax_query_estados]'] = state

            req = requests.post(
                url=url,
                cookies=self.ajax_cookies,
                headers=self.ajax_headers,
                data=self.ajax_data
            )
            data = req.json()

            valid_data = data.get('markers')
            valid_data[0]['id_state'] = state

            ajax_data.append(valid_data)

        return ajax_data

    def get_clinical_info(self):
        ajax_data = self.get_ajax_data()

        clinical_info = []

        for elem in ajax_data:
            num = elem[0].get('id_state')
            url = f'https://dentalia.com/clinica/?jsf=jet-engine:clinicas-archive&tax=estados:{num}'

            response = requests.post(
                url=url,
                params=self.params,
                cookies=self.cookies,
                headers=self.headers,
                data=self.data
            )

            req = response.json()

            data = req.get('data').get('html')

            soup = BeautifulSoup(data, 'lxml')

            for obj in elem:
                obj_id = obj.get('id')
                obj_lat = float(obj.get('latLang').get('lat'))
                obj_lng = float(obj.get('latLang').get('lng'))

                html_class = f'jet-listing-grid__item jet-listing-dynamic-post-{obj_id}'

                data_obj = soup.find('div', class_=html_class)

                clinical_name = data_obj.find('h3', class_='elementor-heading-title elementor-size-default')
                clinical_about = data_obj.find_all('div', class_='jet-listing-dynamic-field__content')

                phone = clinical_about[1].text.replace('Teléfono(s):', '')
                working_hours = clinical_about[2].text.replace('Horario:', '')
                latLang = [obj_lat, obj_lng]

                clinical = {
                    'name': clinical_name.text,
                    'address': clinical_about[0].text,
                    'latlon': latLang,
                    'phone': phone.replace('\n', '').strip().split('\r'),
                    'working_hours': working_hours.replace('\n', '').strip().split('\r')

                }

                clinical_info.append(clinical)

        with open("dentalia.json", 'w', encoding="utf-8") as file:
            json.dump(clinical_info, file, ensure_ascii=False, indent=True)

        return 'successfully'


dentalia = Ajax()

print(dentalia.get_clinical_info())
