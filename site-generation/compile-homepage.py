#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time

# load tables
with open('../cv-data/papers.json') as f:
    papers = json.load(f)
with open('../cv-data/preprints.json') as f:
    preprints = json.load(f)
with open('../cv-data/others.json') as f:
    others = json.load(f)
with open('../cv-data/presentations.json') as f:
    presentations = json.load(f)


#############
# Main Page #
#############

index = open('../index.html', 'w')
index.write(
"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv='content-language' content='en-us'>
    <meta name="description" content="I'm a postdoctoral researcher at TU Wien. I research mathematical logic. This site contains my presentations and publications.">

    <!-- Load simple.css and custom modifications -->
    <link rel="stylesheet" type="text/css" href="simple.css">
    <link rel="stylesheet" type="text/css" href="style.css">

    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <title>Leonardo Pacheco</title>
</head>
<body>
    <header>
        <h1>Leonardo Pacheco</h1>
        <p>Mathematical Logic at the Institute of Science Tokyo</p>
    </header>

    <p>
        I'm a postdoctoral researcher at the Institute of Science Tokyo working with Ryo Kashima. My research is focused on non-classical modal logics, with focus on fixed-point and provability logics.
    </p>

    <!-- -------------------------------- -->
    <h2 id="recent">Recent Presentations</h2>
    <!-- -------------------------------- -->
"""
)
for p in presentations:
    if p['frontPage'] == False:
        continue
    index.write(
        """
        <details>
            <summary>
                “"""
        + p['title']
        + '” at <a href="'
        + p['eventWebsite']
        + '">'
        + p['event']
        + """</a>
            </summary>

            <p>
                """
        + p['abstract']
        + """
            </p>

            <p>
                """
    )
    if p["fullAbstract"] != "":
        index.write(
            '<a href="'
            + p['fullAbstract']
            + """">Full abstract.</a>
                """
        )
    if p["slides"] == "blackboard":
        index.write("Blackboard presentation.")
    elif p["slides"] == "soon":
        index.write("""Slides soon.
            """)
    else:
        index.write(
            '<a href="'
            + p['slides']
            + """">Slides.</a>
            """
        )
    index.write("""</p>
        </details>
""")

index.write("""
        <p>See <a href="presentations.html">here</a> for a full list of presentations.</p>

    <!-- --------------------------------------- -->
    <h2 id="publications">Selected Publications</h2>
    <!-- --------------------------------------- -->
""")

for p in papers:
    if p['frontPage'] == False:
        continue
    authors = [substring.strip() for substring in p['authorList'].split(',')]
    pages = [substring.strip() for substring in p['pages'].split('--')]
    date = [substring.strip() for substring in p['date'].split('-')]

    index.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        index.write(a + ', ')

    index.write("""<a href="https://doi.org/"""
                + p['doi']
                + """">“"""
                + p['title']
                + '”</a>, '
                + p['journal']
                + ", Vol. "
                + p['volume']
                )
    if p['issue'] != "":
        index.write(" ("
                    + p['issue']
                    + ")")
    if p['number'] != "":
        index.write(" No. "
                    + p['number'])
    index.write(", " + pages[0] + "–" + pages[1]+ ", ")
    index.write(date[0] + ".")
    index.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href="https://doi.org/"""
    + p['doi']
    + """">DOI:"""
    + p['doi']
    + """</a>
            </p>
        </details>
"""
    )

for p in preprints:
    if p['frontPage'] == False:
        continue

    authors = [substring.strip() for substring in p['authorList'].split(',')]
    date = [substring.strip() for substring in p['date'].split('-')]

    index.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        index.write(a + ', ')

    index.write("""<a href="https://arxiv.org/abs/"""
                + p['arXiv']
                + """">“"""
                + p['title']
                + '”</a>, arXiv:'
                + p['arXiv']
                + "."
                )
    index.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href="https://arxiv.org/abs/"""
    + p['arXiv']
    + """">arXiv:"""
    + p['arXiv']
    + """</a>
            </p>
        </details>
"""
    )

for p in others:
    if p['frontPage'] == False:
        continue

    authors = [substring.strip() for substring in p['authorList'].split(',')]
    pages = [substring.strip() for substring in p['pages'].split('--')]
    date = [substring.strip() for substring in p['date'].split('-')]

    index.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        index.write(a + ', ')

    index.write("""<a href=" """
                + p['link']
                + """">“"""
                + p['title']
                + '”</a>, '
                + p['journal']
                + ", Vol. "
                + p['volume']
                )
    if p['number'] != "":
        index.write(" ("
                    + p['number']
                    + ")")
    index.write(", " + pages[0] + "–" + pages[1]+ ", ")
    index.write(date[0] + ".")
    index.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href=""" + '"'
    + p['link']
    + """">Link.</a>
            </p>
        </details>
"""
    )

index.write("""
        <p>See <a href="publications.html">here</a> for a full list of publications.</p>

    <!-- ------------------------ -->
    <h2 id="education">Education</h2>
    <!-- ------------------------ -->

        <ul>
            <li>2020-2023: Mathematics PhD at Tohoku University
            <details>
                <summary>Thesis: Exploring the difference hierarchies on \(\mu\)-calculus and arithmetic — from the point of view of Gale–Stewart games</summary>

                <p>Available <a href="./phd_thesis-Leonardo.pdf">here</a>.</p>

                <p>Short abstract: In this thesis, we study two problems related to difference hierarchies.
                The difference hierarchy for a point class \(\Gamma\) classifies the Boolean combinations of sets in \(\Gamma\) by their complexity.
                Gale–Stewart games play essential roles in both problems.</p>

                <p>In the first part of this thesis, we study the \(\mu\)-calculus' alternation hierarchy over various semantics.
                The \(\mu\)-calculus' alternation hierarchy classifies its formulas by how many interdependent fixed-point operators appear in a given formula.
                Bradfield showed that the alternation hierarchy is strict over arbitrary frames.
                This may not happen if we modify the semantics.</p>

                <p>We refine Alberucci and Facchini's proof of the collapse to modal logic over equivalence relations to show that the alternation hierarchy collapses to modal logic in bigger classes of frames.
                We use this characterization to study degrees of ignorance in various epistemic logics.
                Afterwards, we show that, on graded semantics, constructive semantics and modal logic with impossible worlds, the alternation hierarchy collapses to modal logic over equivalence relations.
                On the other hand, the alternation hierarchy is strict on multimodal \(\mu\)-calculus over equivalence relations.
                We also show that current proofs of the collapse do not work on the non-monotone \(\mu\)-calculus.
                Furthermore, we show that the alternation hierarchy collapses to its alternation-free fragment over weakly transitive frames.</p>

                <p>In the second part of this thesis, we study the connection between Gale–Stewart games and reflection principles in second-order arithmetic.
                Gale–Stewart games have been studied in reverse mathematics since its beginning and are central to descriptive set theory.
                Sets definable by the \(\mu\)-calculus are exactly the winning regions of Gale–Stewart games whose payoffs are Boolean combinations of \(\Sigma^0_2\) sets.</p>

                <p>Kołodziejczyk and Michalewski proved that the determinacy of Boolean combinations of \(\Sigma^0_2\) sets is equivalent to the reflection principle \(\Pi^1_3\)-\(\mathrm{Ref}(\Pi^1_2\)-\(\mathsf{CA}_0)\).
                We use finite sequences of coded \(\beta\)-models to prove that the determinacy of Boolean combinations of \(\Sigma^0_1\) sets is equivalent to the reflection principle \(\Pi^1_3\)-\(\mathrm{Ref}(\Pi^1_1\)-\(\mathsf{CA}_0)\).
                We also use the same method to give a new proof of Kołodziejczyk and Michalewski's result.
                At last, we use a modified version of the method to prove that the determinacy of Boolean combinations of \(\Sigma^0_1\) sets of Cantor space is equivalent to the reflection principle \(\Pi^1_2\)-\(\mathrm{Ref}(\mathsf{ACA}_0)\).</p>
            </details></li>
            <li>2018-2020: Mathematics Masters at Tohoku University
            <details>
                <summary>Thesis: On the weak hierarchy of \(\mu\)-calculus</summary>

                <p>Available <a href="./master_thesis-Leonardo.pdf">here</a>.</p>

                <p>In this thesis we present the weak \(\mu\)-calculus and weak \(\mu\)-arithmetic and their alternations hierarchies. We also prove a refinement of a result in Reverse Mathematics related to the \(\mu\)-arithmetic and the determinacy of the finite levels of the difference hierarchy of \(\Sigma^0_2\).</p>
            </details></li>
            <li>2014-2017: Mathematics Major at Universidade Federal de Goiás</li>
            <li>2012-2013: Computer Science Major at Universidade Federal de Goiás (Incomplete)</li>
        </ul>

    <h2 id="contact">Contact</h2>
        <p>
            Mail: leonardovpacheco@gmail.com <br>
            CV: available <a href="./cv.pdf">here</a> <br>
            Blog: <a href="https://leonardopacheco.xyz/blog">https://leonardopacheco.xyz/blog</a>
        </p>
    </body>
    <p>
        This is a picture of me:
    </p>
    <img src="./images/profile_image.jpeg" alt="Picture of a white man with glasses with short brown hair.">

    <footer>Site created by myself, using <a href="https://simplecss.org">Simple.css</a> and <a href="https://mathjax.org">MathJax</a>. Last updated: """
    + time.strftime("%Y-%m-%d")
    + """.</footer>

    <!-- Load MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</html>""")

index.close()





            ################
            # Publications #
            ################




pubs = open('../publications.html', 'w')
pubs.write(
"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv='content-language' content='en-us'>
    <meta name="description" content="I'm a postdoctoral researcher at TU Wien. I research mathematical logic. This site contains my presentations and publications.">

    <!-- Load simple.css and custom modifications -->
    <link rel="stylesheet" type="text/css" href="simple.css">
    <link rel="stylesheet" type="text/css" href="style.css">

    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <title>Leonardo Pacheco - Publications</title>
</head>
<body>
    <header>
        <h1>Leonardo Pacheco</h1>
        <h2>Publications</h2>
    </header>

    <p>
        Ordered from newer to older.
    </p>

    <!-- -------------------------- -->
    <h3>Peer-reviewed Publications</h3>
    <!-- -------------------------- -->

    """
)

for p in papers:
    authors = [substring.strip() for substring in p['authorList'].split(',')]
    pages = [substring.strip() for substring in p['pages'].split('--')]
    date = [substring.strip() for substring in p['date'].split('-')]

    pubs.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        pubs.write(a + ', ')

    pubs.write("""<a href="https://doi.org/"""
                + p['doi']
                + """">“"""
                + p['title']
                + '”</a>, '
                + p['journal']
                + ", Vol. "
                + p['volume']
                )
    if p['issue'] != "":
        pubs.write(" ("
                    + p['issue']
                    + ")")
    if p['number'] != "":
        pubs.write(" No. "
                    + p['number'])
    pubs.write(", " + pages[0] + "–" + pages[1]+ ", ")
    pubs.write(date[0] + ".")
    pubs.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href="https://doi.org/"""
    + p['doi']
    + """">DOI:"""
    + p['doi']
    + """</a>
            </p>
        </details>
"""
    )

pubs.write("""
    <!-- --------- -->
    <h3>Preprints</h3>
    <!-- --------- -->
""")

for p in preprints:
    authors = [substring.strip() for substring in p['authorList'].split(',')]
    date = [substring.strip() for substring in p['date'].split('-')]

    pubs.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        pubs.write(a + ', ')

    pubs.write("""<a href="https://arxiv.org/abs/"""
                + p['arXiv']
                + """">“"""
                + p['title']
                + '”</a>, arXiv:'
                + p['arXiv']
                + "."
                )
    pubs.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href="https://arxiv.org/abs/"""
    + p['arXiv']
    + """">arXiv:"""
    + p['arXiv']
    + """</a>
            </p>
        </details>
"""
    )

pubs.write("""
    <!-- ------------------------------ -->
    <h3>Non-peer-reviewed Publications</h3>
    <!-- ------------------------------ -->
""")

for p in others:
    authors = [substring.strip() for substring in p['authorList'].split(',')]
    pages = [substring.strip() for substring in p['pages'].split('--')]
    date = [substring.strip() for substring in p['date'].split('-')]

    pubs.write(
        """
        <details>
            <summary>
                """
    )
    for a in authors:
        pubs.write(a + ', ')

    pubs.write("""<a href=" """
                + p['link']
                + """">“"""
                + p['title']
                + '”</a>, '
                + p['journal']
                )
    if p['volume'] != "":
        pubs.write(", Vol. "
                    + p['volume']
                    )
    if p['issue'] != "":
        pubs.write(" ("
                    + p['issue']
                    + ")")
    if p['number'] != "":
        pubs.write(" No. "
                    + p['number']
                    + "")
    pubs.write(", " + pages[0] + "–" + pages[1]+ ", ")
    pubs.write(date[0] + ".")
    pubs.write(
    """
            </summary>
            <p>
                """
    + p['abstract']
    + """
            </p>

            <p>
                <a href=""" + '"'
    + p['link']
    + """">Link.</a>
            </p>
        </details>
"""
    )

pubs.write("""
    <p><a href="https://leonardopacheco.xyz">Back</a> to main page.</p>

    <footer>Site created by myself, using <a href="https://simplecss.org">Simple.css</a> and <a href="https://mathjax.org">MathJax</a>. Last updated: """
    + time.strftime("%Y-%m-%d")
    + """.</footer>

    <!-- Load MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</html>""")

pubs.close()





        #################
        # Presentations #
        #################





pres = open('../presentations.html', 'w')
pres.write(
"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv='content-language' content='en-us'>
    <meta name="description" content="I'm a postdoctoral researcher at TU Wien. I research mathematical logic. This site contains my presentations and publications.">

    <!-- Load simple.css and custom modifications -->
    <link rel="stylesheet" type="text/css" href="simple.css">
    <link rel="stylesheet" type="text/css" href="style.css">

    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <title>Leonardo Pacheco - Presentations</title>
</head>
<body>
    <header>
        <h1>Leonardo Pacheco</h1>
        <h2>Presentations</h2>
    </header>

    <p>
        Ordered from newer to older.
    </p>
"""
)

current_year = 3000

for p in presentations:

    p_year = [substring.strip() for substring in p['date'].split('-')][0]
    if int(p_year) < int(current_year):
        current_year = p_year
        pres.write("<h3>" + current_year + "</h3>")

    pres.write(
        """
    <details>
        <summary>
            “"""
    + p['title']
    + '” at <a href="'
    + p['eventWebsite']
    + '">'
    + p['event']
    + """</a>
        </summary>

        <p>
            """
    + p['abstract']
    + """
        </p>

        <p>
            """
    )
    if p["fullAbstract"] != "":
        pres.write(
            '<a href="'
            + p['fullAbstract']
            + """">Full abstract.</a>
            """
        )
    if p["slides"] == "blackboard":
        pres.write("Blackboard presentation.")
    elif p["slides"] == "soon":
        pres.write("""Slides soon.
            """)
    elif p["slides"] != "":
        pres.write(
            '<a href="'
            + p['slides']
            + """">Slides.</a>
        """
        )
    pres.write("""</p>
    </details>
""")

pres.write("""
    <p><a href="https://leonardopacheco.xyz">Back</a> to main page.</p>

    <footer>Site created by myself, using <a href="https://simplecss.org">Simple.css</a> and <a href="https://mathjax.org">MathJax</a>. Last updated: """
    + time.strftime("%Y-%m-%d")
    + """.</footer>

    <!-- Load MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</html>""")

pres.close()