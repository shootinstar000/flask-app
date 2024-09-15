import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import re
def fetch_posts(query: str, headers: Dict[str, str]) -> List[Dict[str, str]]:
    # Construct the search URL
    url = f'https://proxyy.lilbrat387.workers.dev/?s={requests.utils.quote(query)}'
    
    try:
        # Make the HTTP request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        catalog = []

        # Extract data from '.items.full'
        for element in soup.select('.items.full > *'):
            title = element.select_one('.poster img')['alt'] if element.select_one('.poster img') else None
            link = element.select_one('.poster a')['href'] if element.select_one('.poster a') else None
            image = element.select_one('.poster img')['src'] if element.select_one('.poster img') else None
            
            if title and link:
                catalog.append({
                    'title': title,
                    'link': link,
                    'image': image
                })

        # Extract data from '.result-item'
        for element in soup.select('.result-item'):
            title = element.select_one('.thumbnail img')['alt'] if element.select_one('.thumbnail img') else None
            link = element.select_one('.thumbnail a')['href'] if element.select_one('.thumbnail a') else None
            image = element.select_one('.thumbnail img')['src'] if element.select_one('.thumbnail img') else None
            
            if title and link:
                catalog.append({
                    'title': title,
                    'link': link,
                    'image': image
                })

        return catalog

    except requests.RequestException as err:
        print(f'multiMovies error: {err}')
        return []

# Example usage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_info(link: str, headers: Dict[str, str]) -> Dict[str, any]:
    try:
        # Fetch the content of the page
        response = requests.get(link, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Determine the type based on URL
        type_ = 'series' if 'tvshows' in link else 'movie'
        imdb_id = ''  # Placeholder for IMDb ID
        title = link.split('/')[4].replace('-', ' ')
        image = soup.select_one('.g-item a')['href'] if soup.select_one('.g-item a') else ''
        synopsis = soup.select_one('.wp-content p').text if soup.select_one('.wp-content p') else ''
        
        # Initialize links list
        links: List[Dict[str, any]] = []
        
        if type_ == 'series':
            for element in soup.select('#seasons > *'):
                season_title = element.select_one('.title').text.strip() if element.select_one('.title') else ''
                episodes_list = []
                
                for episode in element.select('.episodios > *'):
                    episode_title = 'Episode ' + episode.select_one('.numerando').text.strip().split('-')[1] if episode.select_one('.numerando') else ''
                    episode_link = episode.select_one('a')['href'] if episode.select_one('a') else ''
                    
                    if episode_title and episode_link:
                        episodes_list.append({
                            'title': episode_title,
                            'link': episode_link
                        })
                
                if season_title and episodes_list:
                    links.append({
                        'title': season_title,
                        'directLinks': episodes_list
                    })
        else:
            links.append({
                'title': title,
                'directLinks': [{
                    'title': title,
                    'link': link.rstrip('/'),
                    'type': 'movie'
                }]
            })
        
        # Return the collected information
        return {
            'title': title,
            'synopsis': synopsis,
            'image': image,
            'imdbId': imdb_id,
            'type': type_,
            'linkList': links
        }
    
    except requests.RequestException as err:
        print(f"Error fetching data: {err}")
        return {
            'title': '',
            'synopsis': '',
            'image': '',
            'imdbId': '',
            'type': 'movie',
            'linkList': []
        }


# Define the type for Stream
Stream = Dict[str, Any]

def get_stream(url: str, type_: str, headers: Dict[str, str]) -> List[Stream]:
    try:
        # Fetch the initial page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract necessary attributes
        post_id = soup.select_one('#player-option-1')['data-post'] if soup.select_one('#player-option-1') else ''
        nume = soup.select_one('#player-option-1')['data-nume'] if soup.select_one('#player-option-1') else ''
        type_value = soup.select_one('#player-option-1')['data-type'] if soup.select_one('#player-option-1') else ''
        
        # Determine base URL
        base_url = '/'.join(url.split('/')[:3])
        
        # Prepare the form data for POST request
        form_data = {
            'action': 'doo_player_ajax',
            'post': post_id,
            'nume': nume,
            'type': type_value
        }
        
        # Perform the POST request
        player_res = requests.post(f'{base_url}/wp-admin/admin-ajax.php', headers=headers, data=form_data)
        player_res.raise_for_status()
        player_data = player_res.json()
        
        # Extract the iframe URL
        iframe_html = player_data.get('embed_url', '')
        print("iframe_html content:", iframe_html)  # Debug print

        # Updated regex to handle the iframe URL
        iframe_url_match = re.search(r'src="([^"]+)"', iframe_html, re.IGNORECASE)
        if iframe_url_match:
            iframe_url = iframe_url_match.group(1)
            print("Extracted iframe URL:", iframe_url)  # Debug print
        else:
            print("No iframe URL found in iframe_html")  # Debug print
            iframe_url = None

        if iframe_url and 'multimovies' not in iframe_url:
            iframe_res = requests.get(iframe_url, headers=headers)
            print(iframe_res.text)
            return
            iframe_res.raise_for_status()
            iframe_soup = BeautifulSoup(iframe_res.text, 'html.parser')
            iframe_url = iframe_soup.select_one('.linkserver')['data-video'] or iframe_soup.select_one('#videoLinks').find_all()[0]['data-link']
        
        if iframe_url:
            iframe_res = requests.get(iframe_url, headers=headers)
            iframe_res.raise_for_status()
            iframe_data = iframe_res.text
            
            # Decode the encoded string
            function_regex = re.compile(r'eval\(function\((.*?)\)\{.*?return p\}.*?\(\'(.*?)\'\.split')
            match = function_regex.search(iframe_data)
            p = ''
            if match:
                params = match.group(1).split(',')
                encoded_string = match.group(2)
                p = encoded_string.split("',36,")[0].strip()
                a = 36
                k = encoded_string.split("',36,")[1].slice(2).split('|')
                c = len(k)
                
                while c:
                    c -= 1
                    if k[c]:
                        regex = re.compile(r'\b' + str(c) + r'\b')
                        p = regex.sub(k[c], p)
            
            # Extract the stream URL
            stream_url = re.search(r'file:\s*"([^"]+\.m3u8[^"]*)"', p)
            stream_url = stream_url.group(1) if stream_url else ''
            
            # Extract subtitles
            subtitles = []
            subtitle_matches = re.findall(r'https:\/\/[^\s"]+\.vtt', p)
            for sub in subtitle_matches:
                lang_match = re.search(r'_([a-zA-Z]{3})\.vtt$', sub)
                if lang_match:
                    lang = lang_match.group(1)
                    subtitles.append({
                        'language': lang,
                        'uri': sub,
                        'type': 'VTT',
                        'title': lang
                    })
            
            stream_links = []
            if stream_url:
                stream_links.append({
                    'server': 'Multi',
                    'link': stream_url.replace(r'&i=\d+,.4&', '&i=0.4&'),
                    'type': 'm3u8',
                    'subtitles': subtitles
                })
        
        return stream_links
    
    except requests.RequestException as err:
        print(f'Error fetching data: {err}')
        return []

# Example usage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://proxyy.lilbrat387.workers.dev/movies/the-garfield-movie/'
type_ = 'movie'
streams = get_stream(url, type_, headers)
print(streams)




"""

# Example usage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
link = 'https://proxyy.lilbrat387.workers.dev/movies/the-garfield-movie/'
info = get_info(link, headers)
print(info)


query = 'avengers'  # You can change this to any query you want
posts = fetch_posts(query, headers)
print(posts)
"""
