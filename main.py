import requests

class super_hero_AIP:

    base_host = 'https://akabab.github.io/superhero-api/api'

    def _get_dict_hero(self):
        uri = '/all.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        return response.json()

    def _search_iq_hero(self, list_hero_name=["Hulk", "Captain America", "Thanos"]):
        iq_dict = {}
        hero_dict = self._get_dict_hero()

        for elem in hero_dict:
            if elem["name"] in list_hero_name:
                iq_dict[elem["name"]] = elem["powerstats"]["intelligence"]

        return iq_dict

    def search_max_iq(self, list_hero_name=["Hulk", "Captain America", "Thanos"]):
        list_hero = self._search_iq_hero(list_hero_name)
        return max(list_hero)

if __name__ == '__main__':
    Hero = super_hero_AIP()
    print(Hero._search_iq_hero())
    print(Hero.search_max_iq())