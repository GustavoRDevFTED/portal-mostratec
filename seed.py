from datetime import datetime
from app import create_app
from app.database.mongodb import get_database

app = create_app()

with app.app_context():
    db = get_database()

    categories = [
        {
            "name": "Iniciante",
            "icon": "✳",
            "description": "Projetos introdutórios que demonstram os primeiros passos na criação de soluções tecnológicas.",
            "skills": ["Lógica de programação", "Criatividade e experimentação", "Resolução de problemas básicos"],
            "requirements": "Ênfase no aprendizado, na construção inicial e na explicação das escolhas realizadas.",
            "order": 1,
            "active": True
        },
        {
            "name": "Científico",
            "icon": "⌕",
            "description": "Projetos orientados por pesquisa, investigação e aplicação de metodologia científica.",
            "skills": ["Pesquisa e fundamentação teórica", "Metodologia e análise de dados", "Experimentação e validação"],
            "requirements": "Apresentação do problema, objetivos, método, resultados e referências.",
            "order": 2,
            "active": True
        },
        {
            "name": "Comercial",
            "icon": "↗",
            "description": "Soluções que identificam oportunidades e atendem necessidades de empresas e consumidores.",
            "skills": ["Visão de negócio e mercado", "Proposta de valor", "Viabilidade e experiência do usuário"],
            "requirements": "Demonstração do público-alvo, diferencial, aplicabilidade e potencial de negócio.",
            "order": 3,
            "active": True
        },
        {
            "name": "Embarcado",
            "icon": "⌘",
            "description": "Projetos que integram software e hardware para controlar dispositivos e processos físicos.",
            "skills": ["Eletrônica e microcontroladores", "Sensores e automação", "Integração entre hardware e software"],
            "requirements": "Demonstração do funcionamento físico, componentes e integração do sistema.",
            "order": 4,
            "active": True
        }
    ]

    for category in categories:
        db.categories.update_one(
            {"name": category["name"]},
            {"$set": category},
            upsert=True
        )

    print("Categorias iniciais cadastradas com sucesso.")
