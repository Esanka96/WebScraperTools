import requests

def get_final_url(url, timeout=10):
    try:
        resp = requests.get(url, timeout=timeout,allow_redirects=True)  # follows redirects by default
        final_url = resp.url
        # response.history contains intermediate responses (302/301 etc)
        redirect_chain = [r.headers.get("Location") or r.url for r in resp.history]
        return final_url, redirect_chain
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")

if __name__ == "__main__":
    start = "http://nldxb.njfu.edu.cn"
    final, chain = get_final_url(start)
    print("Redirect chain (intermediate):", chain)
    print("Final URL:", final)
