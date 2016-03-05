# -*- coding: utf-8 -*-
# __templates.py
# =============================
# (c) 2015, Jorge De Los Santos
# ITC-Bypasa
# =============================

"""
LaTeX and HTML templates for pyreport.py
"""

LATEX_TEMPLATE = r"""
\documentclass[12pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\decimalpoint
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{color}
\usepackage{graphicx}
\usepackage{makeidx}
\usepackage{anysize}
\usepackage{pdfpages}
\usepackage[x11names,table]{xcolor}
\usepackage{tikz}
\usepackage{tcolorbox}
\usepackage[hidelinks]{hyperref}
\usepackage{caption}
\usepackage[left=2cm,top=2cm,right=2cm,bottom=2cm]{geometry}
\setlength{\parindent}{0cm}
\tcbset{colback=white!5!white, colframe=gray!10!black, coltitle=black!20!black, 
fonttitle=\bfseries, colbacktitle=white, coltext=gray!30!black}

% Colores
\definecolor{encab_color}{RGB}{200,200,210}
\definecolor{col_ejem}{RGB}{50,50,100}
\definecolor{col_linea}{RGB}{150,150,150}
\definecolor{col_solucion}{RGB}{200,100,100}

\author{Jorge De Los Santos}
\title{Abaqus Report}

\begin{document}
\maketitle

_contents_

\end{document}
"""

CONTENTS_TEMPLATE = r"""
\section{Input data and simulation conditions}

\begin{table}[h]
\centering
\caption{Materials}
\begin{tabular}{P{4cm} P{4cm} P{4cm} P{4cm}}\hline
\textbf{Name} & \textbf{Elastic Modulus} & \textbf{Poisson} & \textbf{Density} \\ \hline
_materialstemplate_
\end{tabular}
\end{table}

\begin{table}[h]
\centering
\caption{Parts}
\begin{tabular}{P{8cm} P{8cm}}\hline
\textbf{Name} & \textbf{Type} \\ \hline
_partstemplate_
\end{tabular}
\end{table}

\begin{table}[h]
\centering
\caption{Instances}
\begin{tabular}{P{6cm} P{6cm} P{6cm}}\hline
\textbf{Name} & \textbf{Nodes} & \textbf{Elements} \\ \hline
_instancestemplate_
\end{tabular}
\end{table}

\begin{table}[h]
\centering
\caption{Steps}
\begin{tabular}{P{4cm} P{4cm} P{4cm} P{4cm}}\hline
\textbf{Name} & \textbf{Time} & \textbf{Frames} & \textbf{Procedure} \\ \hline
_stepstemplate_
\end{tabular}
\end{table}

\begin{table}[h]
\centering
\caption{Job}
\begin{tabular}{P{6cm} P{6cm} P{6cm}}\hline
\textbf{Analysis code} & \textbf{Creation time} & \textbf{Precision}\\ \hline
_jobtemplate_
\end{tabular}
\end{table}

\subsection{Materials curve}

_materialscurvetemplate_


\newpage
\section{Results}

\subsection{Deformed shape}

\begin{center}
\includegraphics[scale=0.6]{_deformedshape_}
\captionof{figure}{Deformed shape}
\end{center}

\subsection{Von Mises Stresses}

\begin{center}
\includegraphics[scale=0.6]{_vonmises_}
\captionof{figure}{Von Mises Stresses}
\end{center}

\begin{center}
\includegraphics[scale=0.6]{_strain_}
\captionof{figure}{Plastic strain}
\end{center}

\subsection{History outputs}
"""

MATERIALS_CURVE_TEMPLATE = r"""
\begin{center}
\includegraphics[scale=0.6]{_materialcurve_}
\captionof{figure}{Material curve of _materialname_}
\end{center}
"""

MATERIALS_TEMPLATE = r"""
\verb|_materialname_| & \verb|_young_| & \verb|_poisson_| & \verb|_density_| \\
"""

PARTS_TEMPLATE = r"""
\verb| _partname_ | & \verb| _parttype_ | \\
"""

INSTANCES_TEMPLATE = r"""
\verb|_instancename_| & \verb|_instancenodes_| & \verb|_instanceelements_| \\
"""

STEPS_TEMPLATE = r"""
\verb|_stepname_| & \verb|_steptime_| & \verb|_stepframes_| & \verb|_stepprocedure_| \\
"""

JOB_TEMPLATE = r"""
\verb|_jobanalysiscode_| & \verb|_jobcreationtime_| & \verb|_jobprecision_| \\
"""


# ============================== HTML TEMPLATES =========================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html Lang="en">
    <head>
        <meta charset='utf-8'>
        <title>Abaqus Report</title>
    </head>
    <body>
        <center><h1>Abaqus Report<h1>
        <h3>Dynamic Explicit Simulation</h3></center>
        
        _contents_
        
    </body>
</html>
"""

CONTENTS_HTML_TEMPLATE = """
    <h3>Materials</h3>

    <table border=1 bordercolor="#7788DD" cellspacing=0 cellpadding=2 bgcolor="#FFFFFF">
        <caption>Materials list</caption>
        <tr>
            <th>Name</th>
            <th>Elastic modulus</th>
            <th>Poisson ratio</th>
            <th>Density</th>
        </tr>
        _materialstemplate_
    </table>
    
    <h3>Parts</h3>
    <table border=1 bordercolor="#7788DD" cellspacing=0 cellpadding=2 bgcolor="#FFFFFF">
        <tr>
            <th>Name</th>
            <th>Type</th>
        </tr>
        _partstemplate_
    </table>
    
    <h3>Instances</h3>
    <table border=1 bordercolor="#7788DD" cellspacing=0 cellpadding=2 bgcolor="#FFFFFF">
        <tr>
            <th>Name</th>
            <th>Nodes</th>
            <th>Elements</th>
        </tr>
        _instancestemplate_
    </table>
    
    <h3>Steps</h3>
    <table border=1 bordercolor="#7788DD" cellspacing=0 cellpadding=2 bgcolor="#FFFFFF">
        <tr>
            <th>Name</th>
            <th>Time</th>
            <th>Frames</th>
            <th>Procedure</th>
        </tr>
        _stepstemplate_
    </table>
    
    <h3>Job</h3>
    <table border=1 bordercolor="#7788DD" cellspacing=0 cellpadding=2 bgcolor="#FFFFFF">
        <tr>
            <th>Analysis code</th>
            <th>Creation time</th>
            <th>Precision</th>
        </tr>
        _jobtemplate_
    </table>
    
    <h2>Results</h2>
    <h3>Deformed shape</h3>
    
    <img src="_deformedshape_" width="400" height="300">

    <h3>Von Mises Stresses</h3>
    
    <img src="_vonmises_" width="400" height="300">
    
    <h3>Plastic strain</h3>
    
    <img src="_pestrain_" width="400" height="300">
    
    <h3>Nominal strain</h3>
    
    <img src="_nestrain_" width="400" height="300">
    
    <h3>Reaction force</h3>
    
    <img src="_rtforce_" width="400" height="300">
"""

MATERIALS_CURVE_TEMPLATE = r"""
\begin{center}
\includegraphics[scale=0.6]{_materialcurve_}
\captionof{figure}{Material curve of _materialname_}
\end{center}
"""

MATERIALS_HTML_TEMPLATE = r"""
        <tr>
            <td>_materialname_</td>
            <td>_young_</td>
            <td>_poisson_</td>
            <td>_density_</td>
        </tr>
"""

PARTS_HTML_TEMPLATE = r"""
        <tr>
            <td>_partname_</td>
            <td>_parttype_</td>
        </tr>
"""

INSTANCES_HTML_TEMPLATE = r"""
        <tr>
            <td>_instancename_</td>
            <td>_instancenodes_</td>
            <td>_instanceelements_</td>
        </tr>
"""

STEPS_HTML_TEMPLATE = r"""
        <tr>
            <td>_stepname_</td>
            <td>_steptime_</td>
            <td>_stepframes_</td>
            <td>_stepprocedure_</td>
        </tr>
"""

JOB_HTML_TEMPLATE = r"""
        <tr>
            <td>_jobanalysiscode_</td>
            <td>_jobcreationtime_</td>
            <td>_jobprecision_</td>
        </tr>
"""

# ==============  SCRIPTS TEMPLATES ================
SCRIPT_GRAPHS_TEMPLATE = r"""
from pyabaqus.pyodb import *

get_nodes_coords(dbpath,find_deformable_body(dbpath),find_last_step(dbpath),fname="dat/nodes.txt")
get_elements_conect(dbpath,find_deformable_body(dbpath),fname="dat/elements.txt")
get_max_eqvs(dbpath,fname="dat/max_eqvs.txt")
get_max_pe(dbpath,fname="dat/max_pe.txt")
get_max_ne(dbpath,fname="dat/max_ne.txt")
get_max_rt(dbpath,fname="dat/max_rt.txt")
"""




