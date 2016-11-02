from tagline_extractor import check_for_new_tagline
from page_constructor import render_page
import boto3


def main():
    filename = 'taglines.txt'
    output_file = 'taglines.html'

    try:
        os.remove(filename)
        os.remove(output_file)
    except OSError:
        pass
    s3_client = boto3.client('s3')
    s3_client.download_file('verge-taglines', filename, filename)

    # grab taglines from s3
    check_for_new_tagline(filename)
    page_html = render_page(filename)

    with open(output_file, 'w') as f:
        f.write(page_html)

    s3_client.upload_file('verge-taglines', output_file, output_file)
    s3_client.upload_file('verge-taglines', filename, filename)

    print ('fin.')

if __name__ == '__main__':
    main()
