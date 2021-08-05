from bs4 import BeautifulSoup
    
    
def generate_urls_text_file(html: str, output_file: str) -> None:
    with open(html, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'html.parser')
        tags = soup.find_all('a')
        for tag in tags:
            with open(output_file, 'a') as file:
                url = str(tag.get('data-href'))
                file.write(f"{url}\n")