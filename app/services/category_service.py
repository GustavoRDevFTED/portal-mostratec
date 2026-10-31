from app.models.category_model import CategoryModel


class CategoryService:

    @staticmethod
    def get_all_categories():
        categories = CategoryModel.get_all()

        if categories:
            return categories

        return [
            {
                "name": "Iniciante",
                "description": (
                    "Categoria destinada a estudantes "
                    "que estão iniciando no desenvolvimento."
                ),
                "skills": [
                    "Lógica de programação",
                    "Algoritmos",
                    "Desenvolvimento básico"
                ]
            },
            {
                "name": "Científico",
                "description": (
                    "Projetos que apresentam pesquisa, "
                    "investigação e desenvolvimento científico."
                ),
                "skills": [
                    "Pesquisa científica",
                    "Metodologia",
                    "Análise de resultados"
                ]
            },
            {
                "name": "Comercial",
                "description": (
                    "Soluções tecnológicas voltadas "
                    "para necessidades reais do mercado."
                ),
                "skills": [
                    "Empreendedorismo",
                    "Inovação",
                    "Viabilidade comercial"
                ]
            },
            {
                "name": "Embarcado",
                "description": (
                    "Projetos que envolvem hardware, "
                    "eletrônica e sistemas embarcados."
                ),
                "skills": [
                    "Microcontroladores",
                    "Eletrônica",
                    "Internet das Coisas"
                ]
            }
        ]