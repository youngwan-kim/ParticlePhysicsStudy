import os

d_ = {
    "The Dirac Equation":15,
    "Interaction by Particle Exchange":3,
    "Electron-Positron Annihilation":12,
    "Electron-Proton Elastic Scattering":8,
    "Deep Inelastic Scattering":8,
    "Symmetries and the Quark Model":10,
    "Quantum Chromodynamics":9,
    "The Weak Interaction":10,
    "The Weak Interactions of Leptons":7,
    "Neutrinos and Neutrino Oscillations":9,
    "CP Violation and Weak Hadronic Interactions":14,
    "Electroweak Unification":5,
    "Tests of the Standard Model":11,
    "The Higgs Boson":13,
}


i = 4
for chname in d_ :

    header = f"""
\\noindent\\rule{{7in}}{{2.8pt}}
\\section{{{chname}}}
    """

    with open(f"Ch{i}.tex",'w') as tex :
        tex.write(header)

    for j in range(0,d_[chname]) :
        prob = f"""
\\begin{{problem}}{{{i}.{j}}}

\\end{{problem}}

\\begin{{solution}}


\\end{{solution}}

\\noindent\\rule{{7in}}{{1.5pt}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

        with open(f"Ch{i}.tex",'a') as tex :
            tex.write(prob)
    i+=1