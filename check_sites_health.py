import sys
import argparse
from urllib.parse import urlparse
from datetime import datetime, timedelta
import whois
import requests


def parse_arguments():
    args_parser = create_parser()
    return args_parser.parse_args()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath",
        type=str,
        required=True,
        help="Please, provide a file path"
    )
    return parser


def load_url_list_from_file(filepath):
    with open(filepath) as file:
        text_to_process = file.read().splitlines()
        return text_to_process


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        return response.ok
    except requests.RequestException:
        return False


def get_domain_name_from_url(url):
    domain_name = urlparse(url).netloc
    return domain_name


def get_domain_expiration_date(domain_name):
    try:
        response = whois.whois(domain_name)
        return response['expiration_date'][0]
    except (AttributeError, IndexError):
        return None


def check_domain_expiration_date(domain_expiration_date, timedelta_limit):
    return datetime.now() + timedelta_limit < domain_expiration_date


def process_url(url):
    is_response_ok = is_server_respond_with_200(url)
    domain_name = get_domain_name_from_url(url)
    domain_expiration_date = get_domain_expiration_date(domain_name)
    is_domain_paid = check_domain_expiration_date(
        domain_expiration_date,
        timedelta(days=30)
    )

    return is_response_ok, domain_name, is_domain_paid


def print_url_info(url, domain_name, is_response_200, is_domain_paid):
    print('URL: {}'.format(url))
    print('With domain name : {}'.format(domain_name))
    print('Respond with status 200 - {}'.format(is_response_200))
    print('Is domain paid? - {}'.format(is_domain_paid))


if __name__ == '__main__':

    args = parse_arguments()

    try:
        url_list = load_url_list_from_file(args.filepath)
    except FileNotFoundError:
        sys.exit("Error has occurred while reading file")

    for url in url_list:

        is_response_ok, domain_name, is_domain_paid = process_url(url)

        print_url_info(
            url, domain_name, is_response_ok, is_domain_paid
        )
