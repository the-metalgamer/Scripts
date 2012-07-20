#!/bin/python3
# -*- coding: utf-8 -*-
import sys
import gnupg
import textwrap
import time

def main(keyring=""):
    gpg = gnupg.GPG(gnupghome=keyring)
    gpg.encoding = "UTF-8"
    publickeys = gpg.list_keys()
    print("<!DOCTYPE html>")
    print("<html>")
    print("\t<head>")
    print("\t\t<title>HaxoGreen Keysigning Party</title>")
    print("\t\t<meta charset=\"UTF-8\" />")
    print("\t\t<meta name=\"description\" content=\"HaxoGreen Keysigning Party organized by C3L\"/>")
    print("\t\t<meta name=\"keywords\" content=\"Keysigning Party, PGP, GPG, HaxoGreen, C3L, Security, Syn2cat, Hackerspace\" />")
    print("\t\t<meta name=\"author\" content=\"the_metalgamer &lt;the_metalgamer@hackerspace.lu&gt;\" />")
    print("\t\t<meta name=\"generator\" content=\"keysigning-list 0.1\" />")
    print("\t</head>")
    print("\t<body>")
    print("\t\t<article>")
    print("\t\t\t<header>")
    print("\t\t\t\t<h1>HaxoGreen Keysigning Party Key-List</h1>")
    now = time.strftime("%H:%M:%S %A, %d of %B %Y")
    pubdate = time.strftime("%Y-%m-%dT%H:%M:%S")
    print("\t\t\t\t<time datetime=\"{}\">Generated on {}</time>".format(pubdate, now))
    print("\t\t\t</header>")
    print("\t\t\t<section>")
    print("""\t\t\t\t<table border="1">""")
    print("\t\t\t\t\t<tr>")
    print("\t\t\t\t\t\t<td>Key-ID</td>")
    print("\t\t\t\t\t\t<td>UID</td>")
    print("\t\t\t\t\t\t<td>Fingerprint</td>")
    print("\t\t\t\t\t\t<td>Length</td>")
    print("\t\t\t\t\t\t<td>Type</td>")
    print("\t\t\t\t\t\t<td>Key Info Matches?</td>")
    print("\t\t\t\t\t\t<td>Owner ID Matches?</td>")
    print("\t\t\t\t\t</tr>")
    for keys in publickeys:
        print("\t\t\t\t\t<tr>")
        print("\t\t\t\t\t\t<td>{}</td>".format(keys["keyid"][-8:]))
        print("\t\t\t\t\t\t<td>", end="")
        for uids in keys["uids"]:
            uid = uids.replace("<","&lt;")
            uid = uid.replace(">","&gt;")
            print("\n" + "\t\t\t\t\t\t\t" + uid + "<br />", end="")
        print()
        print("\t\t\t\t\t\t</td>")
        fingerprint = " ".join(textwrap.wrap(keys["fingerprint"], width=4))
        print("\t\t\t\t\t\t<td>{}</td>".format(fingerprint))
        print("\t\t\t\t\t\t<td>{}</td>".format(keys["length"]))
        if keys["algo"] in ["1","2","3"]:
            algo = "RSA"
        elif keys["algo"] in ["16","20"]:
            algo = "Elgamal"
        elif keys["algo"] in ["17"]:
            algo = "DSA"
        elif keys["algo"] in ["18"]:
            algo = "ECDH"
        elif keys["algo"] in ["10"]:
            algo = "ECDSA"
        else:
            algo = "Unkown"
        print("\t\t\t\t\t\t<td>{}</td>".format(algo))
        print("\t\t\t\t\t\t<td></td>")
        print("\t\t\t\t\t\t<td></td>")
        print("\t\t\t\t\t</tr>")

    print("\t\t\t\t</table>")
    print("\t\t\t</section>")
    print("\t\t\t<footer>")
    print("\t\t\t\t<p>Generated by keysigning-list Version 0.1 by the_metalgamer</p>")
    print("\t\t\t</footer>")
    print("\t\t</article>")
    print("\t</body>")
    print("</html>", end="")

if __name__ == "__main__":
    main(sys.argv[1])