from urllib.parse import urlparse, parse_qs, unquote

url = "viewer.html?v=1761721497516&ptype=0&pdf_url=https%3A%2F%2Fen-cdn.bio-protocol.org%2Fpdf%2FBio-protocol5470.pdf%3Fv%3D1761721497%26rel_link%3DYmlvLXByb3RvY29sLm9yZy9lbi9icGRldGFpbD9pZD01NDcwJnR5cGU9MA%3D%3D%26source%3Dbio"

# Parse query string
parsed = urlparse(url)
query_params = parse_qs(parsed.query)

# Extract and decode the pdf_url
pdf_url_encoded = query_params.get("pdf_url", [""])[0]
pdf_url = unquote(pdf_url_encoded)

print(pdf_url)
