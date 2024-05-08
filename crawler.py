from tools.tools import *
import multiprocessing


if __name__ == "__main__":
    webpages = ['https://example.com', "https://co.computrabajo.com/", "https://www.magneto365.com/co/empleos"]
    with multiprocessing.Pool() as pool:

        results = pool.map(my_function, webpages)

    print(results)
crawl('https://example.com')
