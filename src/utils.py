import json
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - %(levelname)s: %(message)s',
                    filename='../logs/utils.log', encoding='UTF-8',
                    filemode='w')
logger = logging.getLogger('utils')

def get_transactions(path: str) -> list[dict]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info(f'Обращаемся к файлу {path}')
        with open(path, encoding="utf-8") as data_file:
            try:
                transactions_data = json.load(data_file)
                logger.info(f'Данные о финансовых транзакциях получены')
                return transactions_data
            except json.JSONDecodeError:
                logger.error(f'Произошла ошибка декодирования файла')
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error(f'Произошла ошибка: файл не найден')
        print("Файл не найден")
        return []


if __name__ == "__main__":
    print(get_transactions("../data/operations.json"))
