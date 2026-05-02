# Daily ArXiv Papers Summary

Generated: 2026-01-12 19:40:53

---

## 1. Nitrogen enhancement of GN-z11 by metal pollution from supermassive stars

**Authors:** Sho Ebihara, Michiko S. Fujii, Takayuki R. Saitoh, Yutaka Hirai, Yuki Isobe, Chris Nagele

**ArXiv ID:** 2601.04344 (2601.04344v1)

**Abstract:**
Spectroscopic observations by the James Webb Space Telescope (JWST) have revealed young, compact, high-redshift ($z$) galaxies with high nitrogen-to-oxygen (N/O) ratios. GN-z11 at z=10.6 is one of these galaxies. One possible scenario for such a high N/O ratio is pollution from supermassive stars (SMSs), from which stellar winds are expected to be nitrogen-rich. The abundance pattern is determined by both galaxy evolution and SMS pollution, but so far, simple one-zone models have been used. Using a galaxy formation simulation, we tested the SMS scenario. We used a cosmological zoom-in simulation that includes chemical evolution driven by rotating massive stars (Wolf-Rayet stars), supernovae, and asymptotic giant branch stars. As a post-process, we assumed the formation of an SMS with a mass between $10^3$ and $10^5$ $M_\odot$ and investigated the contribution of its ejecta to the abundance pattern. The N/O ratio was enhanced by the SMS ejecta, and the abundance pattern of GN-z11, including carbon-to-oxygen and oxygen-to-hydrogen ratios, was reproduced by our SMS pollution model if the pollution mass fraction ranges within 10-30 per cent. Such a pollution fraction can be realized when the gas ionized by the SMS is polluted, and the gas density is $10^4$-$10^5$ cm$^{-3}$ assuming a Strömgren sphere. We also compared the abundance pattern with those of other N/O-enhanced high-$z$ galaxies. Some of these galaxies can also be explained by SMS pollution.Authors' comments:14 pages, 11 figures, submitted to A&A

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04344)
- [PDF](https://arxiv.org/pdf/2601.04344.pdf)

**Paper Content (Markdown):**

```markdown
_Astronomy & Astrophysics_ manuscript no. main ©ESO 2026

January 9, 2026

## **Nitrogen enhancement of GN-z11 by metal pollution from** **supermassive stars**


S. Ebihara [1], M. Fujii [1], T. Saitoh [2], Y. Hirai [3], H. Umeda [1], Y. Isobe [4] _[,]_ [ 5] _[,]_ [ 6], and C. Nagele [7]


1 Department of Astronomy, The University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-0033, Japan
2 Department of Planetology, Graduate School of Science, Kobe University, 1-1 Rokkodai-cho, Nada-ku, Kobe, Hyogo 657-8501,

Japan
3 Department of Community Service and Science, Tohoku University of Community Service and Science, 3-5-1 Iimoriyama, Sakata,

Yamagata 998-8580, Japan
4 Kavli Institute for Cosmology, University of Cambridge, Madingley Road, Cambridge, CB3 0HA, UK
5 Cavendish Laboratory, University of Cambridge, 19 JJ Thomson Avenue, Cambridge, CB3 0HE, UK
6 Waseda Research Institute for Science and Engineering, Faculty of Science and Engineering, Waseda University, 3-4-1, Okubo,

Shinjuku, Tokyo 169-8555, Japan
7 Department of Physics and Astronomy, Johns Hopkins University, Baltimore, MD 21218, USA


**ABSTRACT**


_Context._ Spectroscopic observations by the James Webb Space Telescope (JWST) have revealed young, compact, high-redshift ( _𝑧_ )
galaxies with high nitrogen-to-oxygen (N/O) ratios. GN-z11 at _𝑧_ = 10 _._ 6 is one of these galaxies.
_Aims._ One possible scenario for such a high N/O ratio is pollution from supermassive stars (SMSs), from which stellar winds are

expected to be nitrogen-rich. The abundance pattern is determined by both galaxy evolution and SMS pollution, but so far, simple

one-zone models have been used. Using a galaxy formation simulation, we tested the SMS scenario.
_Methods._ We used a cosmological zoom-in simulation that includes chemical evolution driven by rotating massive stars (Wolf-Rayet

stars), supernovae, and asymptotic giant branch stars. As a post-process, we assumed the formation of an SMS with a mass between
10 [3] and 10 [5] M⊙ and investigated the contribution of its ejecta to the abundance pattern.
_Results._ The N/O ratio was enhanced by the SMS ejecta, and the abundance pattern of GN-z11, including carbon-to-oxygen and

oxygen-to-hydrogen ratios, was reproduced by our SMS pollution model if the pollution mass fraction ranges within 10–30 per cent.
Such a pollution fraction can be realized when the gas ionized by the SMS is polluted, and the gas density is 10 [4] –10 [5] cm [−][3] assuming a

Strömgren sphere. We also compared the abundance pattern with those of other N/O-enhanced high- _𝑧_ galaxies. Some of these galaxies

can also be explained by SMS pollution.


**Key words.** Galaxies: ISM – Galaxies: evolution – Galaxies: individual: GN-z11 – ISM: abundances – Stars: evolution – Stars:

mass-loss



**1. Introduction**


The James Webb Space Telescope (JWST) has revealed the ex
istence of nitrogen-rich galaxies at high redshift ( _𝑧_ ). A prime

example of such galaxies is GN-z11. The galaxy was identified by the Hubble Space Telescope as having _𝑧_ = 11 _._ 09 [+] - [0] 0 _[.]_ _._ [08] 12
in Oesch et al. (2016), and recent JWST observation updated
its redshift to _𝑧_ = 10 _._ 6 (Bunker et al. 2023; Maiolino et al.

2024b). Several studies have reported that GN-z11 exhibits at
least log(N/O) _>_ −0 _._ 5 (Cameron et al. 2023; Isobe et al. 2023;

Senchyna et al. 2024) from strong nitrogen lines in the rest-frame

ultraviolet, regardless of whether a stellar or AGN radiation

field is assumed. These nitrogen abundances are much higher

than those of local galaxies (Pilyugin et al. 2012; Izotov et al.

2006; Berg et al. 2016, 2019), of which abundances correspond

to the ejecta of core-collapse supernovae (CCSNe) (Nomoto et al.

2013; Watanabe et al. 2024). Such a high N/O ratio in some

high- _𝑧_ galaxies shows rather good agreement with that of glob
ular clusters (GCs) in the Milky Way (Charbonnel et al. 2023;

Senchyna et al. 2024; Ji et al. 2025).

According to the traditional stellar evolution scenario, oxygen

is mainly enriched by CCSNe, whereas carbon and nitrogen are

enriched by stellar winds from asymptotic giant branch (AGB)



stars. D’Antona et al. (2023) and McClymont et al. (2025) have

suggested that AGB stars can be an origin of the N/O-enhanced

gas of GN-z11. However, the main-sequence lifetimes of most

progenitor stars (intermediate- or low-mass stars) are much longer

than the age of high- _𝑧_ galaxies, especially GN-z11, whose stellar
age is estimated to be 24 [+][20]
−10 [Myr (][Tacchella et al. 2023][). On the]
other hand, Rizzuti et al. (2025) assumed an SN-driven galactic

wind model that selectively blows oxygen away after CCSNe.


A possible source of nitrogen that could have been ejected

early on is Wolf-Rayet (WR) stars. In WR stars, the CNO

cycle enriches nitrogen. The stellar wind from WR stars

can also explain the N/O ratio of GN-z11 (Isobe et al. 2023;

Watanabe et al. 2024), but a fine-tuned star formation history

is required (Cameron et al. 2023). Thus, Gunawardhana et al.

(2025) claimed that the WR-only scenario can explain the carbon

enrichment of GN-z11 but not its nitrogen excess. Tidal dis
ruption events (TDEs) are also a possible scenario (Isobe et al.

2023). This scenario requires the existence of a supermassive

black hole. GN-z11 may host an active galactic nucleus (AGN),

but this remains under debate (Bunker et al. 2024; Maiolino et al.

2024b).


Article number, page 1


_A&A proofs:_ manuscript no. main



Another possible source is very massive stars (VMSs) and

supermassive stars (SMSs). VMSs and SMSs are stars with
10 [3] –10 [4] and _>_ 10 [4] M⊙, respectively. So far, no such mas
sive stars have been observed, but they can be formed as

Population (Pop) III stars (Latif et al. 2014; Chon et al. 2018;

Latif et al. 2021; Hirano et al. 2021) or via runaway collisions of

stars (Devecchi & Volonteri 2009; Sakurai et al. 2017; Fujii et al.

2024; Rantala et al. 2024). Although the evolution and yield of

V/SMS have been little studied, Nagele & Umeda (2023) and

Nandal et al. (2024) have proposed that V/SMS can also explain
the N/O ratio of GN-z11 with V/SMS of stars with _𝑍_ = 0 _._ 1 _𝑍_ ⊙

and Pop III stars, respectively. Hereafter, we refer to this V/SMS

scenario simply as the SMS scenario.

Formation of SMSs during the formation of GN-z11-like

galaxies would be expected from their compactness. The half
mass (half-light) radius of GN-z11 is measured to be only 200 pc
(Tacchella et al. 2023). From the mass of 10 [9] M⊙, the half-mass
density of GN-z11 is estimated to be ∼ 100 M⊙ pc [−][3] . Assuming
a power-law density distribution with a power of −2, we expect
10 [6] M⊙ pc [−][3] at ∼ 1 pc. In star cluster formation simulations,

such a high density is shown to result in runaway collision of

stars (Portegies Zwart & McMillan 2002) and the formation of

V/SMSs (Fujii et al. 2024; Rantala et al. 2024). In addition, the

N/O-enhanced population is also known in GCs in the Milky Way

(Charbonnel et al. 2023), and V/SMSs have also been suggested

for GCs (Gieles et al. 2018). Thus, SMS formation in GN-z11
like galaxies seems to be a natural consequence.

Previous numerical studies of N-enrichment due to SMSs

have been performed using one-zone models (Fukushima et al.

2025; Watanabe et al. 2024). However, real galaxies are formed

through more complicated dynamical and chemical evolution.

Saitoh et al. (2025) performed a numerical simulation of galaxy

formation similar to GN-z11. The simulation showed that N/O is

enriched during the first 10–20 Myr after a bursty star formation

due to the stellar winds from rotating massive stars, although the

N/O ratio was slightly lower than that of the observational lower

limit of GN-z11. Since their simulation did not include SMSs, it

remains unclear whether SMSs are responsible for the observed

level of N-enrichment under the realistic environments of galaxy

formation.

In this paper, we test the SMS scenario using the cosmolog
ical simulation results performed in Saitoh et al. (2025). From

the dynamical evolution of the galaxy, we can assume the forma
tion of SMSs as a post-process. In contrast to previous studies

using one-zone models (Fukushima et al. 2025; Watanabe et al.

2024), our 3D-model can trace a spacial distribution of GN-z11
like galaxies, thereby providing a more realistic chemical and

dynamical evolution.

This paper consists of the following sections. In Section 2, the

calculation code and the setup of our galaxy formation simulation

are described. Section 3 states the results of our simulation and

shows how our SMS scenario can realize chemical abundances

similar to those of GN-z11. In Section 4, we discuss whether SMS

scenario can explain other N/O-enhanced galaxies. We summa
rize our research in Section 5.


**2. Method**


_2.1. Numerical simulation_


We adopt the simulation results presented in Saitoh et al. (2025).

Hereafter, we briefly summarize the simulation. The simula
tion was performed using a zoom-in technique for a halo taken

from a cosmological structure formation simulation. The tar

Article number, page 2



get halo is the most massive one in a 100 _ℎ_ [−][1] Mpc [3] volume at
_𝑧_ ∼ 10. Its mass is comparable to the expected mass of GN-z11

(Scholtz et al. 2024). Using MUSIC (Hahn & Abel 2011), the ini
tial condition was generated assuming a standard cosmological
parameters with Planck Collaboration et al. (2020) ( _𝐻_ 0 = 67 _._ 32,
ΩM = 0 _._ 3158, ΩΛ = 0 _._ 6842, Ωb = 0 _._ 04938, and _𝜎_ 8 = 0 _._ 812).
The mass resolutions of 4628 M⊙ and 24972 M⊙ for baryons and

dark matter, respectively, for the zoomed-in region. The softening lengths are _𝜖_ baryon = 5 _._ 7 pc and _𝜖_ DM = 12 _._ 6 pc for baryons

and dark matter, respectively. The boundary particles have larger

masses and softening lengths than those in the zoomed-in region.

The cosmological zoom-in simulation was performed us
ing ASURA (Saitoh et a

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04344.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 2. The early Universe with JWST and ALMA

**Authors:** Rodrigo Herrera-Camus, Natascha Förster Schreiber, Livia Vallini, Rychard Bouwens, John D. Silverman

**ArXiv ID:** 2601.04314 (2601.04314v1)

**Abstract:**
The Atacama Large Millimeter/submillimeter Array and the James Webb Space Telescope are transforming our understanding of galaxy formation and evolution in the early Universe. By combining their capabilities, these observatories provide unprecedented insights into the gas, dust, and stars of high-redshift galaxies at spatially resolved scales, unveiling the complexities of their interstellar medium, kinematics, morphology, active galactic nuclei, and star formation activity. This review summarizes recent breakthroughs in the study of galaxies during the first billion years of cosmic history, highlighting key discoveries, open questions, and current limitations. We discuss how observations, theoretical models, and simulations are shaping our understanding of early galaxy evolution and identify promising directions for future research. While significant progress can be achieved through optimized use of existing facilities and collaborative efforts, further advances will require enhanced angular resolution and sensitivity, motivating upgrades to current instruments and the development of next-generation observatories.Authors' comments:Review Article published in Nature Astronomy. Open access enhanced pdf version: https://rdcu.be/eVPtU. This review summarizes key discoveries and ways forward discussed at the Lorentz Center Workshop, "Synergistic ALMA+JWST View of the Early Universe" (Dec. 2024). 9 pages, 5 figures

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04314)
- [PDF](https://arxiv.org/pdf/2601.04314.pdf)

**Paper Content (Markdown):**

```markdown
**[Review Article                                         https://doi.org/10.1038/s41550-025-02726-0](https://doi.org/10.1038/s41550-025-02726-0)**


**[Review Article                                         https://doi.org/10.1038/s41550-025-02726-0](https://doi.org/10.1038/s41550-025-02726-0)**
# ~~**The early Universe with JWST and ALMA**~~


**Rodrigo Herrera-Camus** **[1,2]** ***, Natascha Förster Schreiber** **[3]** **, Livia Vallini** **[4]** **,**
**Rychard Bouwens** **[5]** **& John D. Silverman** **[6,7,8]**

[*Corresponding author: Rodrigo Herrera-Camus (rhc@udec.cl)](mailto:rhc@udec.cl)


**The Atacama Large Millimeter/submillimeter Array and the James Webb Space**
**Telescope are transforming our understanding of galaxy formation and evolution in**
**the early Universe. By combining their capabilities, these observatories provide**
**unprecedented insights into the gas, dust, and stars of high-redshift galaxies at**
**spatially resolved scales, unveiling the complexities of their interstellar medium,**
**kinematics, morphology, active galactic nuclei, and star formation activity. This**
**review summarizes recent breakthroughs in the study of galaxies during the first**
**billion years of cosmic history, highlighting key discoveries, open questions, and**
**current limitations. We discuss how observations, theoretical models, and**
**simulations are shaping our understanding of early galaxy evolution and identify**
**promising directions for future research. While significant progress can be achieved**
**through optimized use of existing facilities and collaborative efforts, further**
**advances will require enhanced angular resolution and sensitivity, motivating**
**upgrades to current instruments and the development of next-generation**
**observatories.**



Over the past three years, Atacama Large Millimeter/
submillimeter Array (ALMA) and the James Webb Space
Telescope (JWST) have provided an unparalleled multiwavelength view of the gas, dust, and stars in galaxies at
kiloparsec scales, extending our reach from the local
Universe to the first galaxies. The field of galaxy
evolution has entered a golden era: a decade ago, multiwavelength studies of multi-phase gas, dust, and stars at
kiloparsec scales were limited to nearby galaxies. Today,
this capability extends to the first galaxies in the
Universe at redshift _z_ ≈10 and beyond. These observations
now allow us to address fundamental questions by
directly probing the earliest stages of galaxy formation
and evolution: How did galaxies look like in the first
billion years? What were their physical conditions? How
fast and through which pathways were heavy elements,
dust, and central supermassive black holes (SMBHs)
produced? What was the role of gas outflows driven by
feedback from supernovae, massive stars radiation and
winds, and active galactic nuclei (AGN) powered by
accreting SMBHs in regulating star formation activity
and chemical enrichment?

In December 2024, an international group of researchers
working on galaxy evolution gathered at the Lorentz
Center Workshop _Synergistic ALMA+JWST View of the_
_Early Universe_ to examine recent progress enabled by the
combination of these facilities. This review summarizes



key discoveries and ways forward discussed in three main
areas: (1) the interstellar medium (ISM), (2) galaxy
kinematics and structure, and (3) outflows and active
galactic nuclei (AGN).

## **Interstellar Medium**

Figure 1 illustrates how the synergy between ALMA and
JWST allows for a comprehensive study of all major
components of the ISM in star-forming galaxies at _z_ ≳4.
These include the radiation field produced by stars,
ionized gas in HII regions, the interface with neutral gas
in photodissociation regions (PDRs), molecular gas, as
well as interstellar dust, including polycyclic aromatic
hydrocarbons (PAHs), and metals (elements heavier than
He).

Dust profoundly impacts the physics, chemistry, and
observed properties of galaxies. Among the foremost
ALMA discoveries, substantial dust reservoirs have been
unexpectedly detected in systems as distant as _z_ ≈8, when
the universe was merely 600 million years old [1,2,3] . This
finding challenges existing dust formation theories,
calling for a revision of mechanisms such as dust
production in supernova ejecta and grain growth in the
ISM [4,5] . With JWST, measurements of ultraviolet/optical
attenuation curves in galaxies at _z_ ≈7, including the 2175 Å


**Fig. 1 | ALMA and JWST views of stars and the ISM in high-redshift galaxies.** Top: schematic representation of the
interplay between stars, ionized gas in H II regions, neutral gas in PDRs, molecular clouds and dust—including PAHs
—along with the key spectral tracers of these components across the rest-frame UV, optical, infrared and millimetre
wavelengths. Bottom: SED of a typical star-forming galaxy in the local Universe, modelled with CIGALE [98] and
redshifted to _z_ = 5, 8 and 12. The lefthand side highlights the coverage provided by JWST/NIRCam and MIRI
broadband filters, and the spectrograph NIRSpec, enabling studies of the stellar continuum, nebular emission lines
from H II regions, the 2,175-Å PAH extinction feature and the 3.3-µm emission feature for _z_ ≈ 4–6 galaxies. The righthand side shows the spectral coverage of ALMA bands 1–10, which probe dust continuum emission, far-infrared
cooling lines from various ISM phases, and CO transitions tracing molecular gas. Credit: JWST illustration, NASA
GSFC/CIL/



bump [6] traditionally associated with more evolved
galaxies, highlights the rapid emergence of carbonaceous
grains and underscores the efficiency of early dust
production processes. The direct detection of the 3.3 µm
PAH feature in a dusty star-forming galaxy at _z_ ≈4 [7]
reinforces this picture.

JWST and ALMA are shedding new light on the related
issue of how and when the first heavy elements enriched
galaxies in the early universe. The detection of CIII] and



CIV UV emission lines in galaxies just 350 million years
after the Big Bang [8,9] ( _z_ ≈12) suggests that carbon may have
formed much earlier than previously thought, potentially
making it one of the first metals to emerge in the
universe, consistent with observations of carbonenhanced old metal-poor stars in our Galaxy [10] . Detection
of [O III] 88 µm emission in the galaxy JADES-GSz14-0 [11,12] at _z_ ≈14, supported by photometric
measurements of optical [O III] and Hβ lines, indicates
that this system is surprisingly metal-enriched ( _Z≈_ 0.05–


**[Review Article                                         https://doi.org/10.1038/s41550-025-02726-0](https://doi.org/10.1038/s41550-025-02726-0)**



Redshift (z)
6 7 8 9 10 12 14



11 _._ 5


11 _._ 0


10 _._ 5


10 _._ 0









9 _._ 5


1 _._ 0 0 _._ 8 0 _._ 6 0 _._ 4 0 _._ 2

Cosmic Time [Gyr]


**Fig. 2 | High-redshift galaxies observed with ALMA**
**and JWST.** UV luminosity (LUV) as a function of cosmic
time (or redshift) for spectroscopically confirmed
galaxies observed with JWST and with ALMA. The
ALMA sample includes galaxies targeted by the Large
Programs ALPINE [21–23] and CRISTAL [24] (green),
REBELS [25] (red) and the recently awarded PHOENIX
(orange; principal investigator S. Schouws), whose
observations are scheduled for ALMA cycle 12. The
main far-infrared transitions used in each study are also
indicated.


0.2 _Z_ ⊙) only 300 Myr after the Big Bang. These bright
galaxies at _z_ ≳10 show very low dust attenuation, a
phenomenon that cannot be explained solely by dust
destruction but may instead result from outflows
displacing dust to larger distances [13] .

With JWST/NIRSpec, derivation of metallicities up to
_z_ ≈10 via the ‘direct- _T_ e’ method using faint auroral
emission lines now enables new calibrations for strongline diagnostics, important for future large spectroscopic
surveys [14,15] . However, important challenges remain: joint
analyses combining optical ([O II]λλ3726,3729 and

[O III]λ4363) and far-infrared ([O III] 88 µm and [O III]
52 µm) lines show that the direct method may
underestimate metallicities by up to 0.8 dex, due to lowdensity gas not fully traced by optical lines alone [16] .
Recent JWST data at _z_ ≈4–9 further show that electron
densities in early galaxies are significantly higher than at
_z_ ≈0, following approximately _n_ e∝(1 + _z_ ) [1-2], consistent with
high ionization parameters and intense star-formation
surface densities observed at high redshif [17] .
Unexpectedly high N/O ratios found in some galaxies at z
≳ 6 indicate rapid enrichment and possibly unusual stellar
populations [18,19] . The origin of this nitrogen excess
remains uncertain but may provide key insights into early
star formation and feedback [20] .

Among the key gas tracers accessible with ALMA are the

[C II] 158 µm transition, a primary coolant of the cold
neutral ISM, and the [O III] 88 µm transition. As Fig. 2
shows, over the past five years, large ALMA programs —



such as ALPINE [21,22,23] and CRISTAL [24] at _z_ ≈4-6, and
REBELS [25] at _z_ ≈6-8— made headway in measuring these
far-infrared emission lines in massive star-forming
galaxies lying on the stellar mass vs. star formation rate
"main sequence”. These observations show that typical
galaxies at _z_ ≳6 generally exhibit high [O III]/[C II]
luminosity ratios (≳5) [26,27,28], with only a few cases
displaying comparable [C II] and [O III] luminosities [29] .
These findings support models in which intense starburst
episodes drive bright [O III] emission. Cosmological
zoom-in simulations suggest that bursty star formation
may be a key factor in shaping the population of massive,
bright galaxies identified by JWST [30,31], although this
remains debated [32] .

Important challenges remain in constraining dust and
metal properties in high-redshift galaxies. Most dust
estimates rely on a single-band continuum measurement,
leaving large uncertainties in dust temperature ( _T_ dust),
infrared luminosity, and emissivit

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04314.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 3. Through Thick and Thin: The Cosmic Evolution of Disk Scale Height

**Authors:** Si-Yue Yu, Luis C. Ho, Takafumi Tsukui, John D. Silverman, Marc Huertas-Company, Anton M. Koekemoer, Maximilien Franco, Richard Masseyet al.

**ArXiv ID:** 2601.04988 (2601.04988v1)

**Abstract:**
To investigate the formation and evolution of vertical structures in disk galaxies, we measure global $\operatorname{sech}^2$ scale heights, averaging thin and thick components when present, for 2631 edge-on disk galaxies with $M_*>10^{10} M_\odot$ at $0< z < 3.5$ from the JWST COSMOS-Web survey. We show that dust extinction systematically overestimates scale heights at shorter rest-frame wavelengths, and therefore adopt a fixed rest-frame wavelength of 1 $\mu$m. After further correcting for projection-induced bias using a new accurate method, we find that the median disk scale height increases from $0.56\pm0.03$ kpc at $z=3.25$ to $0.84\pm0.04$ kpc at $z=1.25$, and subsequently decreases to $0.67\pm0.06$ kpc at $z=0.25$. The disk length-to-height ratio remains constant at $2.7\pm0.2$ for $z>1.5$, but rises to $4.0\pm0.4$ at $z=0.25$. These results imply that the high-redshift progenitors of present-day thick disks were of intermediate thickness, neither thin nor thick, yet dynamically hot and dense. The observed radial variation of scale height is consistent with the artificial flaring expected from observational effects, disfavoring minor mergers as the primary mechanism of disk thickening. Instead, we suggest that the high-redshift intermediate-thickness disks were single-component systems that increased their vertical scale height through decreasing surface mass density and/or violent gravitational instabilities, eventually producing thick disks. Thin-disk growth begins at $z\approx2$ and dominates at $z\lesssim1$, yielding a vertically more compact system with decreasing scale heights from $z\approx1$ to $0$. The inferred thin-disk mass fraction increases from $0.1\pm0.03$ at $z=1$ to $0.6\pm0.1$ at $z=0$. Together, these findings reveal a continuous evolutionary link between high-redshift single-component disks and present-day thick thin disk systems.Authors' comments:32 pages, 22 figures, and 3 tables. Submitted to ApJS. Revised in response to a positive referee report with only minor comments

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04988)
- [PDF](https://arxiv.org/pdf/2601.04988.pdf)

**Paper Content (Markdown):**

```markdown
Draft version January 9, 2026
Typeset using L [A] TEX **twocolumn** style in AASTeX7.0.1


**Through Thick and Thin: The Cosmic Evolution of Disk Scale Height**


[Si-Yue Yu](http://orcid.org/0000-0002-3462-4175), [1, 2] [Luis C. Ho](http://orcid.org/0000-0001-6947-5846), [3, 4] [Takafumi Tsukui](http://orcid.org/0000-0002-1499-6377), [2] [John D. Silverman](http://orcid.org/0000-0002-0000-6977), [2, 5, 6, 7]


[Marc Huertas-Company](http://orcid.org/0000-0002-1416-8483), [8, 9, 10, 11, 12] [Anton M. Koekemoer](http://orcid.org/0000-0002-6610-2048), [13] [Maximilien Franco](http://orcid.org/0000-0002-3560-8599), [14] [Richard Massey](http://orcid.org/0000-0002-6085-3780), [15]


[Lilan Yang](http://orcid.org/0000-0002-8434-880X), [16] [Rafael C. Arango-Toro](http://orcid.org/0000-0002-0569-5222), [17] [Andreas L. Faisst](http://orcid.org/0000-0002-9382-9832), [18] [Ghassem Gozaliasl](http://orcid.org/0000-0002-0236-919X), [19, 20]


[Kartik Sheth](http://orcid.org/0000-0002-5496-4118), [21] [Jeyhan S. Kartaltepe](http://orcid.org/0000-0001-9187-3605), [16] [Can Xu](http://orcid.org/0000-0002-8437-6659), [22, 23, 2] [Aryana Haghjoo](http://orcid.org/0009-0006-3071-7143), [24] [Xuheng Ding](http://orcid.org/0000-0001-8917-2148), [25, 2]


[Zhaoxuan Liu](http://orcid.org/0000-0002-9252-114X), [2, 6, 5] [and Jacqueline E. McCleary](http://orcid.org/0000-0002-9883-7460) 26


1 _Department of Astronomy, Xiamen University, Xiamen, Fujian 361005, People’s Republic of China_
2 _Kavli Institute for the Physics and Mathematics of the Universe (WPI), The University of Tokyo Institutes for Advanced Study, The_
_University of Tokyo, Kashiwa, Chiba 277-8583, Japan_
3 _The Kavli Institute for Astronomy and Astrophysics, Peking University, 5 Yiheyuan Road, Haidian District, Beijing, 100871, China_
4 _Department of Astronomy, Peking University, 5 Yiheyuan Road, Haidian District, Beijing, 100871, China_
5 _Department of Astronomy, School of Science, The University of Tokyo, 7-3-1 Hongo, Bunkyo, Tokyo 113-0033, Japan_
6 _Center for Data-Driven Discovery, Kavli IPMU (WPI), UTIAS, The University of Tokyo, Kashiwa, Chiba 277-8583, Japan_
7 _Center for Astrophysical Sciences, Department of Physics & Astronomy, Johns Hopkins University, Baltimore, MD 21218, USA_
8 _Instituto de Astrof´ısica de Canarias (IAC), La Laguna, E-38205, Spain_
9 _Observatoire de Paris, LERMA, PSL University, 61 avenue de l’Observatoire, F-75014 Paris, France_
10 _Universit´e Paris-Cit´e, 5 Rue Thomas Mann, 75014 Paris, France_
11 _Universidad de La Laguna. Avda. Astrof´ısico Fco. Sanchez, La Laguna, Tenerife, Spain_
12 _Center for Computational Astrophysics, Flatiron Institute, New York, NY 10010, USA_
13 _Space Telescope Science Institute, 3700 San Martin Drive, Baltimore, MD 21218, USA_
14 _Universit´e Paris-Saclay, Universit´e Paris Cit´e, CEA, CNRS, AIM, 91191 Gif-sur-Yvette, France_
15 _Department of Physics, Centre for Extragalactic Astronomy, Durham University, South Road, Durham DH1 3LE, UK_
16 _Laboratory for Multiwavelength Astrophysics, School of Physics and Astronomy, Rochester Institute of Technology, 84 Lomb Memorial_
_Drive, Rochester, NY 14623, USA_
17 _Aix Marseille Univ, CNRS, CNES, LAM, Marseille, France_
18 _Caltech/IPAC, MS 314-6, 1200 E. California Blvd. Pasadena, CA 91125, USA_
19 _Department of Computer Science, Aalto University, P.O. Box 15400, FI-00076 Espoo, Finland_
20 _Department of Physics, University of, P.O. Box 64, FI-00014 Helsinki, Finland_
21 _Empowered Earth Alliance, Washington, DC 20003, USA_
22 _School of Astronomy and Space Science, Nanjing University, Nanjing, Jiangsu 210093, China_
23 _Key Laboratory of Modern Astronomy and Astrophysics, Nanjing University, Ministry of Education, Nanjing 210093, China_
24 _Department of Physics and Astronomy, University of California, Riverside, 900 University Ave, Riverside, CA 92521, USA_
25 _School of Physics and Technology, Wuhan University, Wuhan 430072, China_
26 _Department of Physics, Northeastern University, 360 Huntington Ave, Boston, MA_


ABSTRACT


To investigate the formation and evolution of vertical structures in disk galaxies, we measure global
sech [2] scale heights, averaging thin and thick components when present, for 2631 edge-on disk galaxies
with _M∗_ _>_ 10 [10] _M⊙_ at 0 _< z <_ 3 _._ 5 from the JWST COSMOS-Web survey. We show that dust
extinction systematically overestimates scale heights at shorter rest-frame wavelengths, and therefore
adopt a fixed rest-frame wavelength of 1 _µ_ m. After further correcting for projection-induced bias using
a new accurate method, we find that the median disk scale height increases from 0 _._ 56 _±_ 0 _._ 03 kpc at
_z_ = 3 _._ 25 to 0 _._ 84 _±_ 0 _._ 04 kpc at _z_ = 1 _._ 25, and subsequently decreases to 0 _._ 67 _±_ 0 _._ 06 kpc at _z_ = 0 _._ 25. The
disk length-to-height ratio remains constant at 2 _._ 7 _±_ 0 _._ 2 for _z >_ 1 _._ 5, but rises to 4 _._ 0 _±_ 0 _._ 4 at _z_ = 0 _._ 25.
These results imply that the high-redshift progenitors of present-day thick disks were of intermediate
thickness, neither thin nor thick, yet dynamically hot and dense. The observed radial variation of
scale height is consistent with the artificial flaring expected from observational effects, disfavoring
minor mergers as the primary mechanism of disk thickening. Instead, we suggest that the high

Email: [phyyueyu@gmail.com (corresponding author: Si-Yue Yu)](mailto:phyyueyu@gmail.com)


2



redshift intermediate-thickness disks were single-component systems that increased their vertical scale
height through decreasing surface mass density and/or violent gravitational instabilities, eventually
producing thick disks. Thin-disk growth begins at _z ≈_ 2 and dominates at _z_ ≲ 1, yielding a vertically
more compact system with decreasing scale heights from _z ≈_ 1 to 0. The inferred thin-disk mass
fraction increases from 0 _._ 1 _±_ 0 _._ 03 at _z_ = 1 to 0 _._ 6 _±_ 0 _._ 1 at _z_ = 0. Together, these findings reveal a
continuous evolutionary link between high-redshift single-component disks and present-day thick thin
disk systems.


_Keywords:_ [High-redshift galaxies (734) — Galaxy kinematics (602) — Galaxy photometry (611) —](http://astrothesaurus.org/uat/734)

[Galaxy stellar disks (1594) — Galaxy structure (622) — Milky Way evolution (1052) —](http://astrothesaurus.org/uat/1594)
Galaxy evolution (594)



1. INTRODUCTION


The thick disk was first identified in 1979 as a diffuse stellar component in edge-on S0 galaxies, distinct
from both the bulge and thin disk (D. Burstein 1979),
and was subsequently recognized in the Milky Way in
1983 through star counts toward the South Galactic Pole
(G. Gilmore & N. Reid 1983). These discoveries established the now-standard view that the Milky Way disk
comprises two components: a thin and a thick disk (K.
Freeman & J. Bland-Hawthorn 2002; T. Bensby et al.
2014; J. Bland-Hawthorn & O. Gerhard 2016).
The formation history of the Milky Way’s disk appears
to have proceeded in two nearly disjoint phases (P. E.
Nissen et al. 2020; M. Xiang & H.-W. Rix 2022; M. Xiang et al. 2025). The thin disk, with an exponential scale
height of _∼_ 0.3–0.4 kpc (M. Juri´c et al. 2008; J. BlandHawthorn & O. Gerhard 2016), is dominated by younger
stars and was formed from the cold gaseous mid-plane
during the phase of steady star formation over the past
_∼_ 8 Gyr (J. Forbes et al. 2012; M. Xiang & H.-W. Rix
2022; S. Yu et al. 2023). The thick disk, with an exponential scale height of _∼_ 0.7–1.2 kpc, consists primarily of old, [ _α_ /Fe]-enhanced stars that originated during
an earlier, bursty star formation phase within the first
_∼_ 5 Gyr (M. Juri´c et al. 2008; T. Bensby et al. 2014; J.
Bland-Hawthorn & O. Gerhard 2016; S. Yu et al. 2021,
2023). Thick disks are now known to be nearly ubiquitous among nearby disk galaxies (P. Yoachim & J. J.
Dalcanton 2006; D. Bizyaev & S. Mitronova 2009; D. V.
Bizyaev et al. 2014; S. Comer´on et al. 2014, 2016, 2018;
G. Kauffmann et al. 2025).
Despite their prevalence, the physical origin of thick
disks remains debated. They may have been born as inherently thick structures under turbulent, gas-rich conditions in the early Universe (F. Bournaud et al. 2009; S.
Yu et al. 2023). Alternative, they may have grown from
initially thin disks through heating by minor mergers or
internal secular processes (P. J. Quinn et al. 1993; A. [´]



Villalobos & A. Helmi 2008; Y. Qu et al. 2011; J. C.
Bird et al. 2021).
Studying galaxy disks across cosmic time provides crucial insight into the mechanisms that construct their vertical structure. In the HST era, the limited spatial resolution made it difficult to distinguish thin and thick
disks, restricting studies to global scale-height measurements. Tracing rest-frame optical to UV wavelength,
B. G. Elmegreen et al. (2017) reported a median global
scale height of 0 _._ 63 kpc, with a scatter of 0 _._ 24 kpc among
individual measurements, at _z ∼_ 2 (see also B. G.
Elmegreen & D. A. Hunter 2006) and detected vertical color gradients that suggest the coexistence of thin
and thick components at early epochs. A later analysis
by K. A. Hamilton-Campos et al. (2023) yielded a median scale height of 0 _._ 74 kpc, with a scatter of 0 _._ 35 kpc,
after correcting for the overestimation caused by projection effect of deviations from perfect edge-on inclination;
however, such corrections depend essentially on the ratio of scale height to scale length, a dependence explored
in this study.
Progress in characterizing disk structure beyond _z ∼_ 1
has recently accelerated thanks to the unprecedented
sensitivity and resolution of JWST’s Near-Infrared
Camera (NIRCam). JWST observations have revealed
a substantial population of regular disk galaxies already
in place within the first few Gyrs, suggesting that disk
assembly and evolution began earlier than previously
thought (L. Ferreira et al. 2023; J. S. Kartaltepe et al.
2023; E. J. Nelson et al. 2023; B. E. Robertson et

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04988.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 4. Symbolically regressing dark matter halo profiles using weak lensing

**Authors:** Alicia Martín, Tariq Yasin, Deaglan J. Bartlett, Harry Desmond, Pedro G. Ferreira

**ArXiv ID:** 2601.05203 (2601.05203v1)

**Abstract:**
The structure of dark matter haloes is often described by radial density profiles motivated by cosmological simulations. These are typically assumed to have a fixed functional form (e.g. NFW), with some free parameters that can be constrained with observations. However, relying on simulations has the disadvantage that the resulting profiles depend on the dark matter model and the baryonic physics implementation, which are highly uncertain. Instead, we present a method to constrain halo density profiles directly from observations. This is done using a symbolic regression algorithm called Exhaustive Symbolic Regression (ESR). ESR searches for the optimal analytic expression to fit data, combining both accuracy and simplicity. We apply ESR to a sample of 149 galaxy clusters from the HSC-XXL survey to identify which functional forms perform best across the entire sample of clusters. We identify density profiles that statistically outperform NFW under a minimum-description-length criterion. Within the radial range probed by the weak-lensing data ($R \sim 0.3 - 3$ h$^{-1}$ Mpc), the highest-ranked ESR profiles exhibit shallow inner behaviour and a maximum in the density profile. As a practical application, we show how the best-fitting ESR models can be used to obtain enclosed mass estimates. We find masses that are, on average, higher than those derived using NFW, highlighting a source of potential bias when assuming the wrong density profile. These results have important knock-on effects for analyses that utilise clusters, for example cosmological constraints on $\sigma_8$ and $\Omega_m$ from cluster abundance and clustering. Beyond the HSC dataset, the method is readily applicable to any data constraining the dark matter distribution in galaxies and galaxy clusters, such as other weak lensing surveys, galactic rotation curves, or complementary probes.Authors' comments:21 pages, 5 figures; submitted to MNRAS

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04314)
- [PDF](https://arxiv.org/pdf/2601.05203.pdf)

**Paper Content (Markdown):**

```markdown
MNRAS **000**, 1–21 (2026) Preprint 9 January 2026 Compiled using MNRAS L [A] TEX style file v3.2

## **Symbolically regressing dark matter halo profiles using weak lensing**


Alicia Martín, [1] _[★]_ Tariq Yasin, [1] Deaglan J. Bartlett, [1] _[,]_ [2] Harry Desmond [3] and Pedro G. Ferreira [1]


1 _Astrophysics, University of Oxford, Oxford, OX1 3RH, United Kingdom_
2 _CNRS & Sorbonne Université, Institut d’Astrophysique de Paris (IAP), UMR 7095, 98 bis bd Arago, F-75014 Paris, France_
3 _Institute of Cosmology & Gravitation, University of Portsmouth, Portsmouth, PO1 3FX, United Kingdom_


Accepted XXX. Received YYY; in original form ZZZ


**ABSTRACT**

The structure of dark matter haloes is often described by radial density profiles motivated by cosmological simulations. These

are typically assumed to have a fixed functional form (e.g. NFW), with some free parameters that can be constrained with

observations. However, relying on simulations has the disadvantage that the resulting profiles depend on the dark matter model

and the baryonic physics implementation, which are highly uncertain. Instead, we present a method to constrain halo density

profiles directly from observations. This is done using a symbolic regression algorithm called Exhaustive Symbolic Regression

(ESR). ESR searches for the optimal analytic expression to fit data, combining both accuracy and simplicity. We apply ESR to

a sample of 149 galaxy clusters from the HSC-XXL survey to identify which functional forms perform best across the entire

sample of clusters. We identify density profiles that statistically outperform NFW under a minimum-description-length criterion.
Within the radial range probed by the weak-lensing data ( _𝑅_ ∼ 0 _._ 3 − 3 h [−][1] Mpc), the highest-ranked ESR profiles exhibit shallow

inner behaviour and a maximum in the density profile. However, the inner slope itself remains weakly constrained due to limited

signal at small radii. As a practical application, we show how the best-fitting ESR models can be used to obtain enclosed mass

estimates. We find masses that are, on average, higher than those derived using NFW, highlighting a source of potential bias

when assuming the wrong density profile. These results have important knock-on effects for analyses that utilise clusters, for

example cosmological constraints on _𝜎_ 8 and Ωm from cluster abundance and clustering. Beyond the HSC dataset, the method

is readily applicable to any data constraining the dark matter distribution in galaxies and galaxy clusters, such as other weak

lensing surveys, galactic rotation curves, or complementary probes.


**Key words:** methods: data analysis – gravitational lensing: weak – dark matter



**1 INTRODUCTION**


In the ΛCDM picture, structure grows hierarchically. Small primor
dial fluctuations are amplified by gravity, first forming small haloes

and then, through accretion and mergers, building ever larger systems

that eventually virialise. At the top of this hierarchy sit galaxy clus
ters. They are the most massive bound objects in the Universe and

are strongly dark-matter dominated (Allen et al. 2011). As such, they

are natural laboratories for testing the properties of dark matter and,

more broadly, for probing possible departures from standard gravity

(Kravtsov & Borgani 2012).

Consequently, clusters are powerful cosmological probes. Their

abundance, when combined with robust mass calibration, places tight

constraints on parameters such as the matter density, Ωm, and the am
plitude of fluctuations, _𝜎_ 8 (Vikhlinin et al. 2009; Abbott et al. 2020).

Beyond abundance statistics, their internal mass profiles encode their

specific assembly histories. These imprints are visible in structural

features like the splashback radius (Diemer & Kravtsov 2014; More

et al. 2015) and in the scaling relations that connect baryons to the

total gravitational field (Chan & DelPopolo 2020; Tian et al. 2020,

2024; Mistele et al. 2025). Therefore, characterising the density pro

_★_ E-mail: alicia.martin@physics.ox.ac.uk


© 2026 The Authors



files of clusters informs both the astrophysics of structure formation

and the underlying cosmological model.

For decades, large-volume cosmological simulations have been the

primary tool for studying the structure of dark matter haloes. Early

_𝑁_ -body simulations consistently showed that haloes exhibit a steep

power-law increase in density toward the centre, known as a “cusp”

(Dubinski & Carlberg 1991; Navarro et al. 1997). This initial finding

appeared to be universal across different simulations and consistent

over a wide range of halo masses, concentrations, and cosmological

models, and was captured by the Navarro-Frenk-White (NFW) profile

(Navarro et al. 1997)


_𝜌_ 0
_𝜌_ ( _𝑟_ ) = _𝑟_ / _𝑟𝑠_ (1 + _𝑟_ / _𝑟𝑠_ ) [2] _[,]_ (1)


where _𝜌_ 0 is a characteristic density and _𝑟𝑠_ a scale radius. The NFW
profile follows a double power law that transitions from _𝜌_ ( _𝑟_ ) ∝ _𝑟_ [−][1]

at small radii to _𝜌_ ( _𝑟_ ) ∝ _𝑟_ [−][3] at large radii.

However, the notion of a universal NFW profile was challenged by

later, higher-resolution dark matter-only simulations, which revealed

more diversity in inner density slopes. For example, the Aquarius

(Navarro et al. 2004) and Via Lactea II (Diemand et al. 2007) simu
lations found that the logarithmic slope becomes progressively shal
lower than −1 toward the centre. In contrast, Moore et al. (1998)
reported a steeper inner slope of _𝜌_ ( _𝑟_ ) ∼ _𝑟_ [−][1] _[.]_ [4] . More recent high

2 _A. Martín et al._


resolution simulations appear to support this steeper behaviour, finding _𝜌_ ( _𝑟_ ) ∼ _𝑟_ [−][1] _[.]_ [5] (Delos et al. 2019; Delos 2025), which they refer

to as a “prompt cusp”. This wider class of generalised NFW models

suggests that factors such as numerical convergence, initial condi
tions or analysis techniques may still influence the inferred inner

slope.

This disagreement has also motivated the development of alterna
tive, more flexible density models. In particular, the Einasto profile

(Einasto 1965), which assumes a power-law form for the logarithmic

density slope (d ln _𝜌_ /d ln _𝑟_ ∝ _𝑟_ _[𝛼]_ ) rather than for the density itself,

was advocated by Navarro et al. (2004) and Merritt et al. (2005). Us
ing high-resolution _𝑁_ -body simulations these works and subsequent

studies (Merritt et al. 2006; Gao et al. 2008; Navarro et al. 2010;

Ludlow et al. 2013) showed that the Einasto model provides a better

fit to halo density profiles than NFW, especially in the inner regions.

Beyond collisionless dynamics, hydrodynamical simulations fur
ther broaden the possibilities: gas cooling and the assembly of the

brightest cluster galaxy (BCG) can contract the dark matter and

steepen inner slopes (Blumenthal et al. 1986; Laporte et al. 2012),

whereas energetic feedback from active galactic nuclei can counteract

or even flatten the central profile (Martizzi et al. 2013a; Peirani et al.

2017). These processes occur on scales close to current resolution

limits and are modelled with subgrid prescriptions, so inferred inner

slopes can depend on both numerical set-ups and baryonic physics

choices (Crain et al. 2015; Sorini et al. 2025).

Another limitation of simulation-based profiles is that they are

phenomenological: they are simple, low-parameter functions cali
brated to match the output of collisionless _𝑁_ -body simulations, rather

than solutions derived from a fundamental theory. In recent years,

however, progress has been made towards a first-principles under
standing. For example, Pontzen & Governato (2013) developed an

analytical framework to study the phase space distribution of cold

dark matter particles based on entropy considerations. Their frame
work reproduces the shallower inner cusp and steep outer decline, in

qualitative agreement with simulated haloes. More recently, Banik

& Bhattacharjee (2025) showed that the NFW profile might emerge

as an attractor solution to a self-consistent theory for collisionless

relaxation. While these works offer some insight on why such pro
files might appear in cold dark matter simulations, their theoretical

motivation is still incomplete.

More significantly, observational data often challenge the uni
versality of the NFW profile, particularly regarding its cuspy inner

structure. On galactic scales, observations of dwarf and low-surface
brightness galaxies suggest a flatter inner density shape, even reach
ing a constant density region known as a “core” (Flores & Primack

1994; Moore 1994; de Blok et al. 2001). On cluster scales, the pic
ture is more complex. While stacked lensing generally favours cuspy

profiles in the 0 _._ 1–2 Mpc regime (Umetsu et al. 2016), detailed anal
yses combining strong lensing with stellar kinematics sometimes

prefer shallower slopes within the inner 10–50 kpc (Sand et al. 2002;

Newman et al. 2011).

Interpreting these potential tensions is difficult. They may arise

from observational systematics within the standard ΛCDM frame
work, such as triaxiality, miscentering, or non-thermal pressure sup
port (Corless & King 2007; Johnston et al. 2007a; Lau et al. 2009).

Alternatively, they may point to new physics. For example, allowing

for self-interacting dark matter (SIDM) can naturally produce core
like profiles that deviate from the standard collisionless prediction

(Spergel & Steinhardt 2000; Rocha et al. 2013; Ragagnin et al. 2024;

Zeng et al. 2025).

These uncertainties highlight the risks of imposing fixed density

templates on observational data. When a single parametric form is as

MNRAS **000**, 1–21 (2026)



sumed, any deviation in the underlying density profile can propagate

directly into biased mass or concentration estimates. For example, in

cluster mass calibration, forcing an NFW profile onto a halo that has

been modified by baryonic feedback or is in a non-equilibrium state

can skew the inferred total mas

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.05203.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 5. Morphologies arising from the gas flow in the innermost kiloparsec of barred galaxy models

**Authors:** Stavros Pastras, Panos A. Patsis, E. Athanassoula

**ArXiv ID:** 2601.04306 (2601.04306v1)

**Abstract:**
Context. We study a series of response models to investigate the formation of specific morphological features in the central 1 kpc region of the gas component in barred spiral galaxies.
  Aims. We aim to understand how structures, such as nuclear rings and spirals, form by varying the parameters of a general gravitational potential and gas properties. Our goal is to determine how much the shape of these structures is driven by the orbital dynamics of the models compared to the influence of the hydrodynamics of the gas. In particular, we examine the effects of the bar strength, bar shape, pattern speed, and central density, as well as their mutual interdependence.
  Methods. We modeled the gas flow using hydrodynamical simulations run with the Eulerian RAMSES code. The underlying gravitational potential was a two-dimensional Ferrers bar and the gas was considered to be isothermal. Alongside analyzing the gas response to the imposed gravitational potentials, we carried out orbital studies for all models. This involved assessing the shapes and stability of periodic orbits and analyzing the distribution of regular versus chaotic regions within the systems.
  Results. The parameters of the gravitational potential alone are insufficient to accurately predict the gas dynamics in a system. The morphology of the gaseous response varies substantially with changes in sound speed, emphasizing the fundamental role of hydrodynamic processes in determining the structure of the gas within the central region. We identify the factors that affect the morphology of nuclear rings and trailing and leading nuclear spirals. The best alignment between our models and structures observed in local barred galaxies is achieved by assuming a sound speed of $c_s=20\,\rm{km\,s^{-1}}$.Authors' comments:18 pages, 23 figures, accepted for publication in A&A

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04306)
- [PDF](https://arxiv.org/pdf/2601.04306.pdf)

**Paper Content (Markdown):**

```markdown
_Astronomy & Astrophysics_ manuscript no. main ©ESO 2026
January 9, 2026

## **Morphologies arising from the gas flow in the innermost kiloparsec** **of barred galaxy models**


S. Pastras [1][,][ 2], P.A. Patsis [3][,][ 2], and E. Athanassoula [4]


1 Max-Planck-Institut für Extraterrestrische Physik (MPE), Gießenbachstr. 1, D-85748 Garching, Germany
e-mail: `spastras@mpe.mpg.de`
2 Max-Planck-Institut für Astrophysik (MPA), Karl-Schwarzschild-Str. 1, D-85748 Garching, Germany
3 Research Center for Astronomy and Applied Mathematics, Academy of Athens, Soranou Efessiou 4, 11527 Athens, Greece
e-mail: `patsis@academyofathens.gr`
4 Aix Marseille Université, CNRS, LAM (Laboratoire d’ Astrophysique de Marseille), UMR 7326, 13388 Marseille 13, France
e-mail: `evangelie.athanassoula@lam.fr`


Received xxxx; accepted xxxx


**ABSTRACT**


_Context._ We study a series of response models to investigate the formation of specific morphological features in the central 1 kpc
region of the gas component in barred spiral galaxies.
_Aims._ We aim to understand how structures, such as nuclear rings and spirals, form by varying the parameters of a general gravitational
potential and gas properties. Our goal is to determine how much the shape of these structures is driven by the orbital dynamics of the
models compared to the influence of the hydrodynamics of the gas. In particular, we examine the effects of the bar strength, bar shape,
pattern speed, and central density, as well as their mutual interdependence.
_Methods._ We modeled the gas flow using hydrodynamical simulations run with the Eulerian `RAMSES` code. The underlying gravitational potential was a two-dimensional Ferrers bar and the gas was considered to be isothermal. Alongside analyzing the gas response
to the imposed gravitational potentials, we carried out orbital studies for all models. This involved assessing the shapes and stability
of periodic orbits and analyzing the distribution of regular versus chaotic regions within the systems.
_Results._ The parameters of the gravitational potential alone are insufficient to accurately predict the gas dynamics in a system.
The morphology of the gaseous response varies substantially with changes in sound speed, emphasizing the fundamental role of
hydrodynamic processes in determining the structure of the gas within the central region. We identify the factors that affect the
morphology of nuclear rings and trailing and leading nuclear spirals. The best alignment between our models and structures observed
in local barred galaxies is achieved by assuming a sound speed of _cs_ = 20 km s [−][1] .


**Key words.** ISM: kinematics and dynamics – Galaxies: kinematics and dynamics – Chaos



**1. Introduction**


The innermost kiloparsec of a galactic bar is its central region,
which in some cases includes an area encircled by a nuclear ring
(see for example Comerón et al. 2010) along with the nuclear
ring itself. Observations provide sufficient information about the
topology and the general morphology of nuclear rings, allowing even for their classification into subclasses (Buta & Combes
1996; Comerón et al. 2010).
However, the area within these rings is less explored. The
primary challenges for observing structures within the innermost
kiloparsec are resolution and projection effects. There are significantly fewer studies that attempt to identify common morphological features in the central regions of galaxies and connect
them to the dynamics of the parent bar.
Notably Martini et al. (2003a,b) used _HST_ images of an extensive galaxy sample to map the distribution of the cold interstellar medium in the central parts of disk galaxies using dust as
a tracer. Among the observed morphologies, they identified nuclear dust spirals, which could be categorized as grand design,
tightly wound, loosely wound, or chaotic (flocculent). In certain
instances, they also detected chaotic circumnuclear dust within
the innermost kiloparsec, or, in some cases, the absence of any
circumnuclear dust structure. Their findings indicated a connec


tion between grand design nuclear spirals and large-scale bars.
Contrarily, they found that tightly wound nuclear spiral arms
are more commonly observed in unbarred galaxies rather than
in barred ones.


Furthermore, Martini et al. (2003a,b) revealed that the majority of barred galaxies do not exhibit rings inside the bar, implying that nuclear spirals are often not situated within a nuclear
ring. In such instances, they are linked directly to the relatively
straight dust lanes that are associated with the large-scale bar. In
such cases, the dust lanes essentially form continuous structures
spanning from scales of several kiloparsecs down to within tens
of parsecs from the galactic center. Such an example is that of
NGC 1530 (see for example Buta 2013, - figure 1-25), in which
a curve is observed in the primary dust lanes of the bar near the
center, without the clear presence of a nuclear ring.


Nevertheless, the regions inside the rings are not always featureless. An example of grand design spiral arms inside a nuclear ring is observed in the recently released _JWST_ image of
NGC 1433. Patsis et al. (2021) identified a nuclear trailing spiral
embedded within the peanut-shaped bulge of NGC 352. Another
example, this time of a multiarmed spiral, is identified inside the
nuclear ring of NGC 1512 as observed by the Hubble space telescope. There are also cases in which the nuclear spiral has three


Article number, page 1


_A&A proofs:_ manuscript no. main



arms, as in the case of NGC 1097, where a three-armed spiral can
be identified inside a nuclear ring (Prieto et al. 2005; Fathi et al.
2006; Davies et al. 2009) (however, see also Kolcu et al. 2023).
Regarding the nuclear rings themselves, in numerous cases
they exhibit a pseudo-ring nature, appearing as an extension of
the primary dust lane shocks. The surface density is not uniform
along a ring and the denser segments are located in the quadrants
that extend inward from the primary shocks. Because of this,
they can be referred to as pseudo-rings. Typical examples can
be observed, for instance, in the SDSS image of NGC 5383, in
the ring of NGC 4736 (van der Laan et al. 2015), or in the _HST_
image of NGC 1512. This class of pseudo-rings can be viewed
as displaying a morphology that lies between those with welldefined nuclear rings and those where the main dust lane shocks
curve inward, extending into the region within 1 kpc.
Another morphological feature associated with the central
regions of barred galaxies, and predicted by the gaseous density
wave theory in its linear approximation (Goldreich & Tremaine
1978, 1979), is the formation of leading spirals. They are expected to appear at the inner inner Lindblad resonance (iILR) region propagating outward (see for example Maciejewski 2004a),
provided that this resonance exists. Nevertheless, there are not
many known examples of leading spirals in the innermost kiloparsec regions of galactic disks. We mention the K [′] image
of NGC 6902 (Grosbøl 2003), which however is a Sa(r) type
galaxy. Díaz et al. (2003) reported the presence of a well-defined
two-armed leading spiral inside a nuclear ring observed in Paα
emission at the core of NGC 1241. In this case, farther inward, a
tiny bar could also be identified.
Central leading spirals have been simulated in analytic models and models of the gas response to bar potentials, under
various assumptions. These spirals are anticipated to manifest
in the gaseous orbits of weak bar potentials, irrespective of
whether the effects of self-gravity are considered (Wada 1994;
Wada & Koda 2001; Maciejewski 2004a). They have been reproduced in hydrodynamical simulations by Ann & Thakur (2005)
using smoothed particle hydrodynamics (SPH), by Kim et al.
(2012b,a) using the grid-based code `CMHOG` (Piner et al. 1995),
by Sormani et al. (2015b) by means of a second-order fluxsplitting scheme (van Albada et al. 1982; Athanassoula 1992b)
and by Li et al. (2015) using the grid-based magnetohydrodynamics code `Athena` (Stone et al. 2008), which utilizes a higherorder Godunov scheme (Stone & Gardiner 2009).
The presence of leading nuclear spirals in models with ILRs
is claimed to be linked to the variation in the precession rate
of elliptical periodic orbits. They emerge when the shape of the
Ω - κ/2 curve in its innermost part is decreasing toward the center. Here, Ω represents the angular frequency and κ denotes the
epicyclic frequency. On the contrary, if this curve increases toward the center, for instance, due to the presence of a central
massive black hole (MBH), the gas forms a trailing spiral. This
scenario is aptly elucidated in Buta & Combes (1996, - figure
79) and Combes (2022, - figure 2).
It is puzzling that nuclear leading spirals are rarely observed
in images of barred spiral galaxies. This is surprising considering that in the typical cases of standard barred galaxy potentials,
the Ω - κ/2 curves tend to decrease toward the center, allowing
the coexistence of an iILR and an outer ILR (oILR) (see e.g.,
Contopoulos 1980, - figure 1) for a wide range of realistic bar
pattern speeds. Nevertheless, it is indeed true that, despite being predicted in some cases, nuclear leading spirals do not form
in all hydrodynamic simulations. This discrepancy may stem either from the extent of the trailing spiral produced at the oILR,
numerical issues related to the simulation itself, such as the reso

Article number, page 2



lution of the numerical scheme employed (Maciejewski 2004b),
or because they are simply a transient feature (Ann & Thakur
2005).
In this study, we investigate the circumstances that lead to
the appearance of all these morphological features within the
central regions of the gaseous components of barred galaxies in
models that do not explicitly include a black hole, represented
by a point mass. Several numerical studies of bar-induced flows
in isothermal gas disks ha

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04306.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 6. Unveiling the 3D structure of the central molecular zone from stellar kinematics and photometry: The 50 and 20 km/s clouds

**Authors:** Francisco Nogueras-Lara, Ashley T. Barnes, Jonathan D. Henshaw, Karl Fiteni, Yoshiaki Sofue, Rainer Schödel, Álvaro Martínez-Arranz, Mattia C. Sormaniet al.

**ArXiv ID:** 2601.05252 (2601.05252v1)

**Abstract:**
The central molecular zone (CMZ), surrounding the Galactic centre, is the largest reservoir of dense molecular gas in the Galaxy. Despite its relative proximity, the 3D structure of the CMZ remains poorly constrained, primarily due to projection effects. We aim to constrain the line-of-sight location of two molecular clouds in the CMZ -- the 50 and 20 km/s clouds -- and to investigate their possible physical connection using stellar kinematics and photometry. This study serves as a pilot for future applications across the full CMZ. We estimated the line-of-sight position of the clouds by analysing stellar kinematics, stellar densities, and stellar populations towards the cloud regions and a control field. We find an absence of westward moving stars in the cloud regions, which indicates that they lie on the near side of the CMZ. This interpretation is supported by the stellar density distributions. The similar behaviour observed in the two clouds, as well as in the region between them (the ridge), suggests that they are located at comparable distances and are physically linked. We also identified an intermediate-age stellar population (2-7 Gyr) in both regions, consistent with that observed on the near side of the CMZ. We estimated the line-of-sight distances at which the clouds and the ridge become kinematically detectable (i.e. where the proper motion component parallel to the Galactic plane differs from that of the control field at the 3 sigma level) by converting their measured proper motions parallel to the Galactic plane using a theoretical model of the stellar distribution. We find that the 50 and 20 km/s clouds are located at $43\pm8$ pc and $56\pm11$ pc from Sgr A*, respectively, and that the ridge lies at $56\pm11$ pc; this supports the idea that the clouds are physically connected through the ridge.Authors' comments:Accepted for publication in A&A. 13 pages, 9 figures

**Links:**
- [Abstract](https://arxiv.org/abs/2601.05252)
- [PDF](https://arxiv.org/pdf/2601.05252.pdf)

**Paper Content (Markdown):**

```markdown
_Astronomy & Astrophysics_ manuscript no. aa56047-25corr_clean ©ESO 2026
January 9, 2026

## **Unveiling the 3D structure of the central molecular zone from** **stellar kinematics and photometry: The 50 and 20 km/s clouds**


Francisco Nogueras-Lara [1][,][ 2,][⋆], Ashley T. Barnes [2], Jonathan D. Henshaw [3][,][ 4], Karl Fiteni [5][,][ 6], Yoshiaki Sofue [7], Rainer
Schödel [1], Álvaro Martínez-Arranz [1], Mattia C. Sormani [5], Jairo Armijos-Abendaño [8], Laura Colzi [9], Izaskun
Jiménez-Serra [9], Víctor M. Rivilla [9], Pablo García [10][,][ 11], Adam Ginsburg [12], Yue Hu [13], Ralf S. Klessen [14][,][ 15][,][ 16][,][ 17],
J. M. Diederik Kruijssen [18], Volker Tolls [16], Alex Lazarian [19], Dani R. Lipman [20], Steven N. Longmore [3][,][ 18], Xing Lu [21][,][ 22],
Sergio Martín [23][,][ 24], Denise Riquelme-Vásquez [25], Jaime E. Pineda [26], Álvaro Sánchez-Monge [27][,][ 28], Arianna Vasini [5], and
Elisabeth A.C. Mills [29]


_(A_ ffi _liations can be found after the references)_


**ABSTRACT**


_Context._ The central molecular zone (CMZ), surrounding the Galactic centre, is the largest reservoir of dense molecular gas in the Galaxy. Despite
its relative proximity, the 3D structure of the CMZ remains poorly constrained, primarily due to projection effects.
_Aims._ We aim to constrain the line-of-sight location of two molecular clouds in the CMZ — the 50 and 20 km/s clouds — and to investigate their
possible physical connection using stellar kinematics and photometry. This study serves as a pilot for future applications across the full CMZ.
_Methods._ We estimated the line-of-sight position of the clouds by analysing stellar kinematics, stellar densities, and stellar populations towards
the cloud regions and a control field.
_Results._ We find an absence of westward moving stars in the cloud regions, which indicates that they lie on the near side of the CMZ. This
interpretation is supported by the stellar density distributions. The similar behaviour observed in the two clouds, as well as in the region between
them (the ridge), suggests that they are located at comparable distances and are physically linked. We also identified an intermediate-age stellar
population (2–7 Gyr) in both regions, consistent with that observed on the near side of the CMZ. We estimated the line-of-sight distances at which
the clouds and the ridge become kinematically detectable (i.e. where the proper motion component parallel to the Galactic plane differs from that
of the control field at the 3σ level) by converting their measured proper motions parallel to the Galactic plane using a theoretical model of the
stellar distribution. We find that the 50 and 20 km/s clouds are located at 43 ± 8 pc and 56 ± 11 pc from Sgr A [∗], respectively, and that the ridge lies
at 56 ± 11 pc; this supports the idea that the clouds are physically connected through the ridge.


**Key words.** Galaxy: nucleus – Galaxy: centre – Galaxy: structure – Galaxy: stellar content – infrared: stars – proper motions – dust, extinction



**1. Introduction**


The central molecular zone (CMZ) is an accumulation of dense
gas at the centre of our Galaxy (e.g. Henshaw et al. 2023). It extends over a radius of ∼ 300 pc (Morris & Serabyn 1996) and
contains 3–5 × 10 [7] M⊙ of dense clouds (Dahmen et al. 1998;
Pierce-Price et al. 2000). This region arguably constitutes the
most extreme star-forming environment in the Milky Way (Lu
et al. 2019; Henshaw et al. 2023; Hatchfield et al. 2024) and
is characterised by high temperatures (Ginsburg et al. 2016;
Krieger et al. 2017), strong turbulence (Federrath et al. 2016;
Kauffmann et al. 2017; Henshaw et al. 2019), an intense magnetic field (e.g. Crutcher et al. 1996; Pillai et al. 2015; Hu et al.
2022; Lu et al. 2024), and high confining pressures (Yamauchi
et al. 1990; Spergel & Blitz 1992; Muno et al. 2004).
The CMZ is shaped by gas funnelled through the Galactic
bar (e.g. Sormani & Barnes 2019) and likely gave rise to the nuclear stellar disc (NSD) — an old (≳ 8 Gyr), dense, and massive
(∼ 10 [9] M⊙) structure at the Galactic centre. The NSD has a scale
length of ∼ 100 pc and a scale height of ∼ 40 pc (e.g. GallegoCano et al. 2020; Sormani et al. 2022), and it partially overlaps
with the CMZ (e.g. Launhardt et al. 2002; Nogueras-Lara et al.
2020). The CMZ also hosts Sagittarius A [∗] (Sgr A [∗] ), the supermassive black hole at the centre of the Milky Way (e.g. Gravity


⋆ E-mail: `fnogueras@iaa.es`



Collaboration et al. 2018, 2020; Event Horizon Telescope Collaboration et al. 2022).
Despite its relative proximity (the Galactic centre is located
at ∼ 8.25 kpc; e.g. Reid et al. 2019; Gravity Collaboration et al.
2018, 2020), deriving the CMZ structure is extremely challenging due to projection effects along the line of sight towards the
Galactic centre (e.g. Battersby et al. 2025a). Determining the 3D
distribution of its gas is essential for: (1) understanding the formation of the NSD and its ongoing growth via newly formed
stars; (2) pinpointing molecular clouds and star-forming regions
to better comprehend their behaviour in the context of CMZ dynamics (Henshaw et al. 2023); (3) tracing gas flows towards the
central black hole to estimate mass transfer rates (Schoedel et al.
2023); and (4) revealing the interactions between gas, stars, and
the central black hole (GRAVITY Collaboration et al. 2021).
Efforts to determine the geometry of the CMZ have focused
on converting the projected distribution of cloud positions and
their line-of-sight velocities into a face-on morphological model
(see Henshaw et al. 2023, and references therein). While it is
generally accepted that the CMZ gas follows an eccentric, ringlike, or toroidal structure, its precise geometry is still under debate. Three main models have been proposed: (a) a two-armed
spiral (Sofue 1995; Sawada et al. 2004; Ridley et al. 2017), (b)
closed elliptical orbits (Molinari et al. 2011; Walker et al. 2025;
Lipman et al. 2025), and (c) open streams (Kruijssen et al. 2015).
Several key molecular clouds are placed differently in existing


Article number, page 1 of 13


_A&A proofs:_ manuscript no. aa56047-25corr_clean


**Fig. 1.** Upper panel: Central ∼ 12 [′] × 30 [′] of the GALACTICNUCLEUS _JHKs_ survey (Nogueras-Lara et al. 2019), covering the 50 and 20 km/s
clouds (credit: ESO/Nogueras-Lara et al.). The positions of the 50 and 20 km/s clouds are indicated, along with Sgr A [∗] and the young stellar
clusters Arches and Quintuplet. Lower panel: Control field (red box), where high-extinction regions (white shaded contours) are excluded, along
with the 50 and 20 km/s clouds (dashed white regions) and the nuclear star cluster (NSC; dotted white region), assuming an effective radius of
∼ 4 pc (Schödel et al. 2014a; Gallego-Cano et al. 2020).



models of the CMZ structure (Fig. 3 in Henshaw et al. 2023).
In particular, the locations of the 50 and 20 km/s clouds (Kauffmann et al. 2017; Nogueras-Lara et al. 2021c; Henshaw et al.
2023; Battersby et al. 2025b) remain unclear, with each model
placing them at different positions along the line of sight. Determining their location is thus essential to help distinguish between
competing models, and also to assess whether they interact with
Sgr A [∗] and supply material via gas inflow (e.g. Liu et al. 2012;
Lopez et al. 2016; Tress et al. 2020).


In this work we combined stellar kinematics and photometry to investigate the line-of-sight location of the 50 and 20 km/s
clouds. This is possible thanks to the overlap between the NSD
and the CMZ (e.g. Launhardt et al. 2002), which enables precise
stellar photometry and astrometry even through high-extinction
regions (e.g. Nogueras-Lara et al. 2019; Libralato et al. 2021).
Our study builds on previous analyses of the Brick cloud (e.g.
Nogueras-Lara et al. 2021c; Martínez-Arranz et al. 2022) and
represents a step forward since we are able to estimate line-ofsight distances. This work serves as a pilot study for our methodology, which will later be applied to the full CMZ to reconstruct
its 3D morphology and assess which of the existing models — if
any — best describes its actual structure.


Article number, page 2 of 13



**2. Data**


Figure 1 shows the central ∼ 12 [′] × 31 [′] region (∼ 28 pc × 72 pc, at
the Galactic centre distance) of the NSD. This area includes the
50 and 20 km/s clouds, whose line-of-sight positions we aimed
to estimate. To identify stars associated with these clouds, we
used the H2 column density map from Battersby et al. (2025a,b)
and defined the regions by selecting contours of _N_ (H2) = 1.1 ×
10 [23] cm [−][2] that outline the clouds as shown in Fig. 2 of Battersby
et al. (2025a) and in our Fig. 1.
We also defined a control field within the same area, at similar Galactic longitude and latitude as the target clouds, avoiding
regions with high extinction that are not representative of the
typical NSD population. For this purpose, we used the 4.5 µm
extinction map from Schödel et al. (2014a), which provides uniform coverage across the field. At this wavelength, dust extinction is relatively low, allowing us to probe dense clouds and reliably identify high-extinction areas. We analysed the extinction
distribution and excluded regions with values above the 70th
percentile. In addition, we removed the target areas associated
with the 50 and 20 km/s clouds, as well as the nuclear star cluster, whose stellar population differs from that of the NSD (e.g.
Schödel et al. 2020; Nogueras-Lara et al. 2021b; FeldmeierKrause 2022; Chen et al. 2023). The final control region, along


Nogueras-Lara et al.: The 3D Structure of the CMZ: The 50 and 20 km/s Clouds


with the excluded areas, is shown in the bottom panel of Fig. 1.
As a cross-check for our analysis in the following sections, we
also used the full region (excluding the shaded contours in the
same panel) as a secondary, larger control field.


_2.1. Photometry_



We used the _HKs_ photometry from the GALACT

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.05252.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 7. Formation of Recycled Pulsars in Common Envelope Binaries

**Authors:** Yu-Dong Nie, Yong Shao, Jian-Guo He, Ze-Lin Wei, Shi-Jie Gao, Xiao-Jie Xu, Xiang-Dong Li

**ArXiv ID:** 2601.04355 (2601.04355v1)

**Abstract:**
We present a systematic study of the evolution of low- and intermediate-mass X-ray binaries (L/IMXBs) consisting of a $1.4\,M_{\odot}$ neutron star (NS) and a donor star of mass $1-8\,M_{\odot}$. Using grids of detailed MESA simulations, we show that for donor masses of $2-8\,M_{\odot}$, mass transfer may be dynamically unstable, leading to a common envelope (CE) phase. By adopting CE ejection efficiencies in the range $\alpha_{\rm CE} = 0.3-3.0$, we find that post-CE binaries frequently experience a CE decoupling phase (CEDP), which plays a critical role in determining their final orbital and compositional properties. Systems with initial donor masses $\gtrsim 3.5\,M_{\odot}$ predominantly evolve into NS binaries with carbon-oxygen or oxygen-neon white dwarfs (WDs) with masses between $0.5\,M_{\odot}$ and $1.4\,M_{\odot}$. Comparison with the observed population of binary pulsars with a WD companion shows better agreement with higher CE ejection efficiencies ($\alpha_{\rm CE} = 3.0$). Furthermore, we demonstrate that NSs can accrete a sufficient amount of matter ($\gtrsim 0.01\,M_{\odot}$) during the CEDP and subsequent Case BA/BB/BC mass transfer phases to be effectively recycled into millisecond pulsars. We identify two distinct evolutionary channels capable of reproducing the observed characteristics of the millisecond pulsar PSR J1928+1815 with a helium-star companion. Our results highlight the importance of the CEDP in the formation of recycled pulsars and provide constraints on the CE ejection efficiency during binary evolution.Authors' comments:13 pages, 8 figures, accepted for publication in ApJ

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04314)
- [PDF](https://arxiv.org/pdf/2601.04355.pdf)

**Paper Content (Markdown):**

```markdown
Draft version January 9, 2026
Typeset using L [A] TEX **twocolumn** style in AASTeX631


**Formation of Recycled Pulsars in Common Envelope Binaries**


[Yu-Dong Nie,](http://orcid.org/0009-0009-4482-6350) [1, 2] [Yong Shao,](http://orcid.org/0000-0003-2506-6906) [1, 2] [Jian-Guo He,](http://orcid.org/0000-0003-3862-0726) [1, 2] [Ze-Lin Wei,](http://orcid.org/0009-0001-4454-8428) [1, 2] [Shi-Jie Gao,](http://orcid.org/0000-0002-0822-0337) [1, 2] [Xiao-Jie Xu,](http://orcid.org/0000-0002-3614-1070) [1, 2] and


[Xiang-Dong Li](http://orcid.org/0000-0002-0584-8145) [1, 2]


1 _Department of Astronomy, Nanjing University, Nanjing 210023, People’s Republic of China_
2 _Key Laboratory of Modern Astronomy and Astrophysics, Nanjing University, Ministry of Education, Nanjing 210023, People’s Republic_
_of China_


ABSTRACT


We present a systematic study of the evolution of low- and intermediate-mass X-ray binaries
(L/IMXBs) consisting of a 1 _._ 4 _M⊙_ neutron star (NS) and a donor star of mass 1 _−_ 8 _M⊙_ . Using
grids of detailed MESA simulations, we show that for donor masses of 2 _−_ 8 _M⊙_, mass transfer may
be dynamically unstable, leading to a common envelope (CE) phase. By adopting CE ejection efficiencies in the range _α_ CE = 0 _._ 3 _−_ 3 _._ 0, we find that post-CE binaries frequently experience a CE
decoupling phase (CEDP), which plays a critical role in determining their final orbital and compositional properties. Systems with initial donor masses ≳ 3 _._ 5 _M⊙_ predominantly evolve into NS binaries
with carbon-oxygen or oxygen-neon white dwarfs (WDs) with masses between 0 _._ 5 _M⊙_ and 1 _._ 4 _M⊙_ .
Comparison with the observed population of binary pulsars with a WD companion shows better agreement with higher CE ejection efficiencies ( _α_ CE = 3 _._ 0). Furthermore, we demonstrate that NSs can
accrete a sufficient amount of matter (≳ 0 _._ 01 _M⊙_ ) during the CEDP and subsequent Case BA/BB/BC
mass transfer phases to be effectively recycled into millisecond pulsars. We identify two distinct evolutionary channels capable of reproducing the observed characteristics of the millisecond pulsar PSR
J1928+1815 with a helium-star companion. Our results highlight the importance of the CEDP in
the formation of recycled pulsars and provide constraints on the CE ejection efficiency during binary
evolution.


_Keywords:_ Binary stars; X-ray binary stars; Neutron stars; White dwarf stars; Stellar evolution



1. INTRODUCTION


Pulsars, the observational manifestations of neutron
stars (NSs), have been a subject of intense study since
the first radio pulsar was discovered by A. Hewish et al.
(1968). To date, over 3000 radio pulsars have been detected in the Milky Way, among which more than 200
are recycled pulsars residing in binary systems. This
indicates that binary evolution plays a significant role
in the formation of recycled pulsars. Systems containing a recycled pulsar and a white dwarf (WD) are
widely considered to be the evolutionary endpoints of
low- and intermediate-mass X-ray binaries (L/IMXBs,
T. M. Tauris & E. P. J. van den Heuvel 2023). Approximately 200 LMXBs have been observed in our Galaxy
(Q. Z. Liu et al. 2007; S. Chaty 2022), primarily located
in the Galactic bulge and globular clusters (e.g., J. van


[shaoyong@nju.edu.cn](mailto: shaoyong@nju.edu.cn)



Paradijs & N. White 1995). In contrast, only a handful
of IMXBs have been identified, largely due to their relatively short-lived mass transfer (MT) phases ( _∼_ 1000 yr)
and the absorption of X-rays by the dense gas surrounding the accreting NSs (E. P. J. van den Heuvel 1975).
Investigating the evolution of IMXBs is essential for understanding the origin of binary pulsars with massive
carbon-oxygen (CO) or oxygen-neon (ONe) WD companions. In L/IMXBs, the accretion of mass and angular momentum can spin up NSs into rapidly rotating
pulsars via the so-called recycling process (e.g., T. M.
Tauris & E. P. J. van den Heuvel 2023).
The canonical formation channels for binaries hosting
a recycled pulsar are well established. An initial binary
system consisting of a high-mass primary and a lowmass secondary may undergo a common envelope (CE)
phase, provided the primary is sufficiently massive to
end its life as an NS. Following the CE phase, the naked
helium (He) star may engage in further MT phase. If the


2


binary remains bound after the primary undergoes a supernova explosion, an LMXB forms. Close-orbit LMXBs
lose angular momentum via magnetic braking and gravitational wave radiation, causing their orbits to shrink.
If the donor star is hydrogen rich and always remains
Roche-lobe filling, the binary evolves to become a converging system (E. Pylyser & G. J. Savonije 1988; A. G.
Istrate et al. 2014). Additionally, LMXBs with a narrow
range of initial orbital periods can evolve into binaries
containing a low-mass HeWD (M. V. van der Sluys et al.
2005; A. G. Istrate et al. 2014). This outcome is sensitive to input physics, particularly the treatment of magnetic braking (e.g., A. G. Istrate et al. 2014; K. X. Van
& N. Ivanova 2019; Z.-L. Deng et al. 2021; H.-L. Chen
et al. 2021; S.-J. Gao et al. 2022; Y.-N. Fan et al. 2024).
Furthermore, the formation of recycled pulsar _−_ HeWD
binaries has also been linked to wide-orbit LMXBs (S.
Rappaport et al. 1995; T. M. Tauris & G. J. Savonije
1999; P. Podsiadlowski et al. 2002; J. Lin et al. 2011; Y.
Shao & X.-D. Li 2012; K. Jia & X.-D. Li 2016; S.-J. Gao
& X.-D. Li 2023; B. Wang et al. 2024).
Analogous to LMXBs, an initial binary with a highmass primary and an intermediate-mass secondary can
evolve into an IMXB if it survives the supernova explosion associated with NS formation. Close-orbit IMXBs
typically undergo Case A MT (where Roche-lobe overflow, RLOF, occurs during the donor’s core hydrogen burning) or early Case B MT (RLOF during the
Hertzsprung gap phase), ultimately yielding a binary
with a recycled pulsar and a HeWD or a COWD companion (T. M. Tauris et al. 2000; Y. Shao & X.-D. Li
2012). For wider-orbit IMXBs, RLOF commences when
the donor ascends the giant branch or a later evolutionary stage. This MT phase is often dynamically unstable,
leading to a CE phase during which the NS becomes
engulfed by the donor’s envelope (B. Paczynski 1976;
E. P. J. van den Heuvel 1976). A recycled pulsar with
a COWD companion can form from such a CE-evolving
IMXB (E. P. J. van den Heuvel 1994), highlighting the
pivotal role of CE evolution in IMXB outcomes.
The CE evolutionary scenario, as proposed by B.
Paczynski (1976) and reviewed by N. Ivanova et al.
(2013), outlines two critical aspects: the initial conditions for triggering CE evolution related to MT stability (e.g., G. E. Soberman et al. 1997; H. Ge et al.
2010, 2015, 2020; K. Pavlovskii et al. 2017; Z.-W. Han
et al. 2020; Y. Shao & X.-D. Li 2014, 2021; P. Marchant
et al. 2021) and the final outcomes related to the balance between orbital decay and envelope ejection (e.g.,
R. F. Webbink 1984; G. Nelemans & C. A. Tout 2005;
N. Soker 2015; J. Klencki et al. 2021; A. Vigna-G´omez
et al. 2022; R. Hirai & I. Mandel 2022; R. Di Stefano



et al. 2023). Although binary pulsar formation channels
have been studied for decades, the detailed impact of CE
evolution remains an active area of research. Previous
works (e.g., T. M. Tauris et al. 2011; C. Zhu et al. 2015;
J.-G. He et al. 2024) often relied on analytic parameterizations for CE outcomes, underscoring the need for
detailed simulations to accurately determine CE properties. By modeling the evolution of high-mass X-ray
binaries through a CE phase, Y.-D. Nie et al. (2025) recently identified a new post-CE evolutionary stage—the
common envelope decoupling phase (CEDP)—providing
a valuable framework for probing CE and post-CE evolution.
Using the updated CE scheme of P. Marchant et al.
(2021), Y.-D. Nie et al. (2025) performed simulations for
binary systems containing a 1 _._ 4 _M⊙_ NS and an 8 _−_ 20 _M⊙_
donor star, following evolution until core carbon depletion. In this paper, we similarly simulate a grid of NS
L/IMXBs, focusing on systems that undergo CE phases,
and compare our theoretical results with observational
data from binary pulsars.


2. METHOD


We employ the Modules for Experiments in Stellar Astrophysics (MESA) code (version 12115, B. Paxton et al. 2011, 2013, 2015, 2018, 2019; A. S. Jermyn
et al. 2023) to conduct our binary evolution simulations. Each model is initialized with a zero-age mainsequence (ZAMS) donor star and an NS of mass _M_ NS [i] [=]
1 _._ 4 _M⊙_ . We construct a comprehensive grid of models spanning initial donor masses _M_ d [i] [from 1] _[ M][⊙]_ [to]
8 _M⊙_ in increments of 0 _._ 5 _M⊙_, and initial orbital periods covering _−_ 0 _._ 3 _≤_ log10( _P_ orb [i] _[/]_ [d)] _[ ≤]_ [3] _[.]_ [5 in steps of]
0.1. Following Y.-D. Nie et al. (2025), the metallicity is set to be _Z_ = 0 _._ 0142. Simulations are evolved
until terminated by numerical limits, including: (1)
logQ ~~l~~ imit = 5, (2) gamma ~~c~~ enter ~~l~~ imit = 1000, and
(3) max ~~n~~ umber ~~r~~ etries = 15000. Notably, we do not
impose a maximum model number, as this could prematurely halt evolution before WD formation.
In our calculations, we adopt the mixing length theory
of E. B¨ohm-Vitense (1958), the Ledoux criterion for convection (P. Ledoux 1947), and the default overshooting
parameter in MESA. Nuclear reaction rates are taken
from R. H. Cyburt et al. (2010) and C. Angulo et al.
(1999). Stellar winds are modeled using the Dutch prescription (E. Glebbeek et al. 2009), which incorporates
wind models from C. de Jager et al. (1988), J. S. Vink
et al. (2001), and T. Nugis & H. J. G. L. M. Lamers
(2000) for different stellar types. Wind accretion onto
the NS is treated via the Bondi-Hoyle mechanism (H.
Bondi & F. Hoyle 1944). We use the updated MT pre

scription of P. Marchant et al. (2021), which based on
the Roche-lobe radius fitting formula of P. P. Eggleton
(1983). We assume that mass accretion onto the NS is
l

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04355.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 8. Investigating HII Regions in the Disk of NGC 7331 with the Circumgalactic H$\alpha$ Spectrograph

**Authors:** Nazende Ipek Kerkeser, Nicole Melso, David Schiminovich, Erika Hamden, Meghna Sitaram, Ignacio Cevallos-Aleman

**ArXiv ID:** 2601.04322 (2601.04322v1)

**Abstract:**
We investigate the ionized gas kinematics of HII regions in the disk of NGC 7331 using integral field unit data collected with the Circumgalactic H$\alpha$ Spectrograph (CH$\alpha$S). NGC 7331 is a well-studied nearby galaxy with HII regions resolved by seeing-limited observations, making it ideally suited for this work. The galaxy disk features vigorous star formation, especially in the central ring of starburst activity. We present a catalog of 136 HII regions detected in the SIRTF Nearby Galaxies Survey (SINGS) H$\alpha$ image. Using this refined catalog, we perform aperture photometry on the SINGS narrowband H$\alpha$ images of NGC 7331, extracting the H$\alpha$ luminosity L(H$\alpha$) of these regions. We present corresponding measurements of the average line-of-sight ionized gas velocity dispersion $\sigma$ in these HII regions with CH$\alpha$S. High-resolution velocity and dispersion maps of the galactic disk are produced from the CH$\alpha$S spectral imaging, selecting spaxels with high signal to noise in order to measure velocity dispersions as low as 12 km s$^{-1}$. Our measurements of the L(H$\alpha$), $\rm \Sigma_{SFR}$ and $\sigma$ in NGC 7331 are consistent with spatially resolved observations of HII regions in large surveys of nearby galaxies. We explore the L(H$\alpha$)$- \sigma$ relationship, identifying turbulent HII regions with nonthermal dispersions likely driven by stellar feedback. The dispersion is correlated with the star formation rate surface density, and using the relation $\rm \sigma\propto \epsilon\Sigma_{SFR}^\alpha$, HII regions in NGC 7331 are best fit by $\epsilon= 80$ , $\alpha=0.285$.Authors' comments:15 pages, 6 figures, 2 tables, Accepted for publication in ApJ

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04322)
- [PDF](https://arxiv.org/pdf/2601.04322.pdf)

**Paper Content (Markdown):**

```markdown
Draft version January 9, 2026
Typeset using L [A] TEX **twocolumn** style in AASTeX7.0.1


**Investigating H** II **Regions in the Disk of NGC 7331 with the Circumgalactic H** _α_ **Spectrograph**


[Nazende ipek Kerkeser](http://orcid.org/0009-0006-0229-2221), [1] [Nicole Melso](http://orcid.org/0000-0002-4895-6592), [1, 2] David Schiminovich, [3, 4] [Erika Hamden](http://orcid.org/0000-0002-3131-7372), [1] [Meghna Sitaram](http://orcid.org/0000-0001-7714-6137), [3, 4]


[and Ignacio Cevallos-Aleman](http://orcid.org/0000-0001-8255-7424) 4, 5


1 _Steward Observatory, University of Arizona, 933 N. Cherry Avenue, Tucson, AZ 85721, USA_
2 _School of Physics and Astronomy, Rochester Institute of Technology, 84 Lomb Memorial Drive, Rochester, NY 14623, USA_
3 _Department of Astronomy, Columbia University, 550 W. 120th Street, MC 5246, New York, NY 10027, USA_
4 _Columbia Astrophysics Laboratory, Columbia University, 550 W. 120th Street, MC 5247, New York, NY 10027, USA_
5 _Department of Physics, Columbia University, 538 W. 120th Street, 704 Pupin Hall, MC 5255, New York, NY 10027, USA_


ABSTRACT


We investigate the ionized gas kinematics of H ii regions in the disk of NGC 7331 using integral
field unit data collected with the Circumgalactic H _α_ Spectrograph (CH _α_ S). NGC 7331 is a wellstudied nearby galaxy with H ii regions resolved by seeing-limited observations, making it ideally
suited for this work. The galaxy disk features vigorous star formation, especially in the central ring
of starburst activity. We present a catalog of 136 H ii regions detected in the SIRTF Nearby Galaxies
Survey (SINGS) H _α_ image. Using this refined catalog, we perform aperture photometry on the SINGS
narrowband H _α_ images of NGC 7331, extracting the H _α_ luminosity L(H _α_ ) of these regions. We present
corresponding measurements of the average line-of-sight ionized gas velocity dispersion _σ_ in these H ii
regions with CH _α_ S. High-resolution velocity and dispersion maps of the galactic disk are produced from
the CH _α_ S spectral imaging, selecting spaxels with high signal to noise in order to measure velocity
dispersions as low as 12 km s _[−]_ [1] . Our measurements of the L(H _α_ ), ΣSFR and _σ_ in NGC 7331 are
consistent with spatially resolved observations of H ii regions in large surveys of nearby galaxies. We
explore the L(H _α_ ) _−σ_ relationship, identifying turbulent H ii regions with nonthermal dispersions likely
driven by stellar feedback. The dispersion is correlated with the star formation rate surface density,
and using the relation _σ ∝_ _ϵ_ Σ _[α]_ SFR [, H][ ii][ regions in NGC 7331 are best fit by] _[ ϵ]_ [ = 80,] _[ α]_ [ = 0] _[.]_ [285.]


_Keywords:_ [HII regions (694) — Interstellar line emission (844) — Spectroscopy (1558) — Spiral galaxies](http://astrothesaurus.org/uat/694)
(1560)



1. INTRODUCTION


H ii regions are vital tracers of recent star formation, and they provide key insight into the interactions
between stellar feedback and the interstellar medium
(ISM). The ISM across redshifts is supersonically turbulent (Glazebrook 2013; Ubler et al. 2019 [¨] ; Bacchini
et al. 2020; Rizzo et al. 2024), driven by a combination
of internal and external processes including stellar feedback (winds, supernovae), gravitational and magnetic
instabilities, galactic shear, and accretion (Elmegreen &
Scalo 2004; Glazebrook 2013, and references therein).
Turbulence in the ISM plays a crucial role in regulating
star formation, providing global pressure support that
counteracts gravity while also creating perturbations


Corresponding author: Nicole Melso

[nxmsps@rit.edu](mailto: nxmsps@rit.edu)



that provoke small-scale collapse (Mac Low & Klessen
2004).
Turbulent motions in the ISM are observationally
probed using the gas velocity dispersion, with many
studies finding a positive correlation between gas dispersion ( _σ_ ) and the luminosity (L) or star formation rate
(Lehnert et al. 2009, 2013; Green et al. 2010, 2014; Le
Tiran et al. 2011; Moiseev et al. 2015). This correlation,
known as the L _−σ_ relation, is expected for many models of ISM turbulence (Lehnert et al. 2009; Krumholz &
Burkhart 2016). The L _−σ_ relationship has been studied
extensively in high-redshift galaxies and local luminous
and ultraluminous infrared galaxies with high star formation rates and large gas dispersions (e.g., Bellocchi
et al. 2013; Arribas et al. 2014; Green et al. 2014; Ubler [¨]
et al. 2019; Perna et al. 2022) where gravitational instability, gas transport, and external accretion likely contribute significantly to turbulence (Krumholz et al. 2018;


2


Ginzburg et al. 2022; Mai et al. 2024). Galaxies with
lower star formation rates around a few solar masses per
year may straddle the boundary between gravity-driven
turbulence and stellar feedback-driven models where the
ionized gas dispersions are dominated by the internal
motions of the H ii regions, highlighting the importance
of spatially resolved measurements of the L _−σ_ relation
in this regime at low-redshifts (Krumholz & Burkhart
2016).
NGC 7331 provides an interesting mixture of environments for investigating the relationship between star
formation and ISM gas kinematics, aided by its close
proximity and extensive observation history. Multiwavelength observations have identified distinct morphological features in NGC 7331. The galactic disk is bright in
H _α_ emission and hosts a large population of H ii regions
(Rubin et al. 1965; Hodge & Kennicutt 1983; Marcelin
et al. 1994; Petit 1998). A prominent central ring of
dust and gas is seen in CO (Young & Scoville 1982),
H i (Bosma 1978), IR (Telesco et al. 1982; Regan et al.
2004), and H _α_ (Battaner et al. 2003). This ring exhibits starburst activity that accounts for a significant
fraction of the galaxy’s total star formation (Battaner
et al. 2003; Thilker et al. 2007). Some kinematic studies
of NGC 7331 suggest a counterrotating bulge relative
to the disk (Prada et al. 1996), and peculiar velocities
at the inner boundary of the central ring are consistent
with ionized gas inflow (Battaner et al. 2003). A largescale warp in the H i gas distribution (Bosma 1978),
an extended distribution of debris/plumes/streams surrounding the galaxy, as well as a a large population
of dwarf companions, all suggest a history of mergers and tidal interactions (Ludwig et al. 2012; Blauensteiner et al. 2017). Complex velocity structure and
morphology, combined with enhanced star formation in
NGC 7331, provide an ideal setting for studying how
star formation influences and is influenced by gas kinematics.
In this paper, we study the integrated properties of
136 H ii regions across the disk of NGC 7331 using integral field spectroscopy (IFS). IFS is a crucial observational technique for efficiently studying large catalogs
of H ii regions in great detail (e.g., S´anchez et al. 2012;
Espinosa-Ponce et al. 2020; McLeod et al. 2020; Cosens
et al. 2022; Law et al. 2022; Congiu et al. 2023; Groves
et al. 2023; Rickards Vaught et al. 2024). At the distance of NGC 7331 (14.5 Mpc; Freedman et al. 2001)
the instrument spatial resolution of 2 _[′′]_ _._ 5 corresponds to
approximately 175 pc (70 pc arcsec _[−]_ [1] ), allowing for the
identification of individual H ii regions throughout the
disk. The H ii regions studied in this work have a radius
of _∼_ 200 pc on average. We examine the kinematics of



these H ii regions, focusing on the relationship between
the H _α_ luminosity and ionized gas velocity dispersion
( _σ_ ).
This paper is outlined as follows. Section 2 describes
the photometric and spectroscopic datasets and the data
reduction process. Section 3 outlines the selection and
characterization of the H ii regions in our catalog. Section 4 presents the ionized gas morphology in the disk
of NGC 7331 and analyzes the H _α_ L _−σ_ relation. In
Section 5, we interpret our findings in the context of existing literature and theoretical models. Section 6 concludes with a summary of key results and directions for
future research.


2. OBSERVATIONS


This work relies on a combination of photometric and
spectroscopic datasets, detailed below. NGC 7331 has
a wealth of multiwavelength observations, and many of
these datasets have aided our analysis. Here, we map
the spatiokinematic structure of ionized gas throughout
the galactic disk of NGC 7331 in great detail.


2.1. _Circumgalactic Hα Spectrograph Observations_


Spectroscopic data were collected with the recently
commissioned Circumgalactic H _α_ Spectrograph (CH _α_ S;
Melso et al. 2022). CH _α_ S is an advanced IFS optimized
for mapping the spatial and kinematic structure of ultrafaint, ionized gas. Accordingly, CH _α_ S can easily detect high-surface-brightness H _α_ emission from H ii regions in the galactic disk, resolving complex morphology that can be difficult to fully capture with long-slit
spectroscopy. En route to ultradeep observations probing the diffuse outskirts of galaxies, CH _α_ S will provide
detailed spatial and kinematic characterization of the
dense ISM. The maps of NGC 7331 presented in this
work are an early demonstration of the full observing
power of CH _α_ S.
CH _α_ S operates with a resolving power of _R ∼_ 10 _,_ 000,
a field of view (FOV) of 10 _[′]_ _×_ 10 _[′]_, and a spatial resolution of 2 _[′′]_ _._ 5. The entrance to the IFS is a microlens array, which segments the telescope focal plane and which
leads to the formation of _>_ 60,000 spectra, each dispersed over a narrow bandpass to avoid overlap. The
spatial resolution is set by the pitch of the microlens
array, which is slightly larger than the average seeing.
In Figure 1 we present spectral imaging of NGC 7331
in H _α_ emission. A summary of the CH _α_ S observations is
given in Table 1. These data were collected during the
Fall of 2023, under very dark, photometric conditions
with _<_ 2% Moon illumination and _>_ 125 _[◦]_ Moon separation. The stack shown in Figure 1 consists of 21, 360s
exposu

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04322.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 9. sidmkit: A Reproducible Toolkit for SIDM Phenomenology and Galaxy Rotation-Curve Modeling

**Authors:** Nalin Dhiman

**ArXiv ID:** 2601.04735 (2601.04735v1)

**Abstract:**
Self-interacting dark matter (SIDM) is a well-motivated extension of cold dark matter that can modify halo structure on galactic and group scales while remaining consistent with large-scale structure. However, practical SIDM work often requires bridging several layers, including microphysical scattering models, velocity-dependent effective cross sections, phenomenological astrophysical constraints, and (separately) data-driven halo fits, such as rotation curves. In this paper, we describe \texttt{sidmkit}, a transparent and reproducible Python package designed to support SIDM ``micro$\rightarrow$macro'' calculations and to provide a robust batch pipeline for fitting rotation curves in the SPARC data. On the SIDM side, \texttt{sidmkit} implements velocity-dependent momentum-transfer cross sections for a Yukawa interaction using standard analytic approximations (Born, classical, and Hulthén-based) with a numerical partial-wave option for spot checks. It also provides consistent velocity-moment averaging for Maxwellian relative speeds, scattering-rate utilities, and curated literature \emph{summary} constraints for regression tests and exploratory scans. On the rotation-curve side, we implement bounded non-linear least squares fits of NFW and Burkert halo models to SPARC baryonic decompositions, with optional mass-to-light priors and information-criterion summaries (AIC/BIC). For the demonstration dataset, we process 191 \texttt{rotmod} galaxies (LTG+ETG bundles) and fit both NFW and Burkert models (382 total fits). We find that Burkert is preferred by $\Delta\mathrm{BIC} > 0$ for $65.4\%$ of galaxies, with ``strong'' preference ($\Delta\mathrm{BIC}>6$) in $32.5\%$ of galaxies;Authors' comments:12 pages, 13 figures, Methods and software paper; includes a reproducible SPARC rotation-curve fitting pipeline and SIDM phenomenology utilities

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04735)
- [PDF](https://arxiv.org/pdf/2601.04735.pdf)

**Paper Content (Markdown):**

```markdown
## **sidmkit: A Reproducible Toolkit for SIDM** **Phenomenology and Galaxy Rotation-Curve Modeling**

Nalin Dhiman


School of Computing and Electrical Engineering

Indian Institute of Technology Mandi, India

```
               d24008@students.iitmandi.ac.in

```

January 9, 2026


**Abstract**


Self-interacting dark matter (SIDM) is a well-motivated extension of cold dark matter
that can modify halo structure on galactic and group scales while remaining consistent
with large-scale structure. However, practical SIDM work often requires bridging several
layers, including microphysical scattering models, velocity-dependent effective cross sections,
phenomenological astrophysical constraints, and (separately) data-driven halo fits, such
as rotation curves. In this paper, we describe `sidmkit`, a transparent and reproducible
Python package designed to support SIDM “micro _→_ macro” calculations and to provide a
robust batch pipeline for fitting rotation curves in the SPARC data. On the SIDM side,
`sidmkit` implements velocity-dependent momentum-transfer cross sections for a Yukawa
interaction using standard analytic approximations (Born, classical, and Hulth´en-based) with
a numerical partial-wave option for spot checks. It also provides consistent velocity-moment
averaging for Maxwellian relative speeds, scattering-rate utilities, and curated literature
_summary_ constraints for regression tests and exploratory scans. On the rotation-curve side,
we implement bounded non-linear least squares fits of NFW and Burkert halo models to
SPARC baryonic decompositions, with optional mass-to-light priors and information-criterion
summaries (AIC/BIC). For the demonstration dataset, we process 191 `rotmod` galaxies
(LTG+ETG bundles) and fit both NFW and Burkert models (382 total fits). We find
that Burkert is preferred by ∆BIC _>_ 0 for 65 _._ 4% of galaxies, with “strong” preference
(∆BIC _>_ 6) in 32 _._ 5% of galaxies; NFW is strongly preferred in 14 _._ 7%. Median reduced
_χ_ [2] values are 1 _._ 25 (NFW) and 0 _._ 71 (Burkert) for cases with positive degrees of freedom.
These results summarise phenomenological fit quality and should _not_ be interpreted as a
direct SIDM measurement without a careful treatment of baryonic, geometric, and selection
systematics.We stress reproducibility and honesty with reviewers: the package is meant to
be a reliable starting point, not a claim of definitive astrophysical inference. The toolkit is
an open-source Python package that the community can use to do analyses and add to it.

### **1 Introduction**


The standard cold dark matter (CDM) paradigm has been remarkably successful on large scales;
however, on galactic scales, several long-discussed tensions, such as the cusp-core problem and
the diversity of rotation curves, motivate a careful scrutiny of dark matter microphysics and
baryonic modelling. One minimal extension is self-interacting dark matter (SIDM), where dark
matter particles scatter elastically with a cross section per unit mass _σ/m_ that can be velocity
dependent [1–3]. In many SIDM models, scattering is efficient in dwarf and low-surface-brightness
galaxies but suppressed in clusters, potentially producing cored density profiles in some systems
while remaining consistent with cluster bounds [4, 5].
Turning SIDM from an idea into a quantitative analysis is, in practice, a workflow problem.
A typical study requires: (i) a microphysical model (e.g., Yukawa-mediated scattering), (ii) a


1


mapping from particle parameters to velocity-dependent effective cross sections, (iii) astrophysical
observables that depend on velocity moments (not just _σ/m_ at a single _v_ ), (iv) halo-level quantities
such as scattering rates and core formation radii, and (v) independent empirical constraints
or likelihoods from clusters, dwarfs, and rotation curves. Different papers often implement
overlapping pieces with slightly different conventions, units, and numerical approximations,
making reproduction and cross-checking difficult.
In parallel, rotation-curve datasets such as SPARC [6] provide high-quality measurements
and baryonic decompositions that are invaluable for testing halo phenomenology. Even when
one is not performing a direct SIDM microphysical inference, robust batch fitting of standard
halo profiles (cuspy and cored) is a useful calibration and sanity check layer.
This work introduces `sidmkit`, a small but rigorous toolkit aimed at _transparent_ SIDM
micro _→_ macro calculations and _reproducible_ batch rotation-curve fits. The goals are:


  - **Correctness-first** : stable units, explicit assumptions, and built-in regression benchmarks;


  - **Modularity** : microphysics, averaging, constraints, halo utilities, and SPARC fitting are
separated but composable;


  - **Honest scope** : provide baseline tools and summaries without overstating inference.

### **2 Software overview**


`sidmkit` is distributed as a standard Python package with both an importable API and a
command-line interface (CLI). The design philosophy is to keep the public API small and to
make most workflows runnable from the CLI for reproducibility. The main components are:


1. **Microphysics layer:** Yukawa model definition and _σT_ ( _v_ ) computation.


2. **Velocity averaging:** numerical evaluation of _⟨σv_ _[n]_ _⟩/m_ for Maxwellian relative speeds.


3. **Constraint layer:** curated _summary_ constraints and simple point-likelihood helpers.


4. **Halo utilities:** scattering rate estimates and an illustrative _r_ 1 core-formation radius
calculation.


5. **SPARC batch fitter:** NFW and Burkert fits to `rotmod` files with chunking ( `--skip`,
`--limit` ) and merged population reports.


The package relies primarily on `NumPy` and `SciPy` for numerics [9, 10] and optionally
`Matplotlib` for plotting [11]. All results in this paper are reproducible using the commands in
Appendix A.

### **3 SIDM microphysics layer**


**3.1** **Yukawa interaction model**


We consider elastic scattering of identical dark matter particles of mass _mχ_ mediated by a
Yukawa potential with mediator mass _mϕ_ and coupling _αχ_,

_V_ ( _r_ ) = _±_ _[α][χ]_ (1)

_r_ _[e][−][m][ϕ][r][,]_


where the sign corresponds to attractive or repulsive interactions. This non-relativistic potential
is a common effective description for a range of SIDM models [2].


2


**3.2** **Transfer cross section**


Astrophysical observables are often more directly sensitive to the momentum-transfer cross
section,

                _σT ≡_ _d_ Ω(1 _−_ cos _θ_ ) _[dσ]_ (2)

_d_ Ω _[,]_


which suppresses forward scattering. (Some contexts use alternative angular weights for identical
particles; `sidmkit` focuses on _σT_ as the default because it matches the convention of many
astrophysical summaries [3].)


**3.3** **Regimes and approximations**


Exact Yukawa scattering requires solving the Schr¨odinger equation, but standard approximations
capture the main behaviour in most of parameter space [2]. `sidmkit` implements:


  - **Born regime:** valid for _αχmχ/mϕ ≪_ 1. The implementation follows the closed-form
momentum-transfer expression used widely in the SIDM literature (see `sidmkit.cross` ~~`s`~~ `ections`
for the exact expression).


  - **Classical regime:** valid when the de Broglie wavelength is short compared to the
interaction range. We use a standard piecewise approximation for _σT_ ( _β_ ) where _β ∝_
_αχmϕ/_ ( _mχv_ [2] ).


  - **Resonant / Hulth´en approximation:** in parts of the non-perturbative regime, the
Yukawa potential can be approximated by a Hulth´en potential to capture resonant features.


  - **Partial-wave (numerical) option:** a direct phase-shift computation used for spot checks
and debugging. It is _not_ recommended for large parameter scans without care, because it
is slower and can fail in extreme resonant regions if the ODE solver requires prohibitively
small step sizes.


A practical point: any “auto” regime selection is necessarily heuristic near regime boundaries. `sidmkit` therefore exposes the method choice explicitly and emits warnings when the
dimensionless coupling _αχmχ/mϕ_ is near unity.


**3.4** **Velocity averaging**



Many astrophysical constraints depend on velocity moments such as _⟨σT v⟩/m_ . For isotropic
Maxwellian one-particle velocities with 1D dispersion _σ_ 1d, the _relative_ speed distribution is
Maxwellian with mean _⟨v_ rel _⟩_ = 4 _σ_ 1d _/_ _[√]_ ~~_π_~~ . We define the _n_ -th moment

        - _σT vn_         -         - _∞_ _[σ][T]_ [ (] _[v]_ [)] _[n]_




_[T]_

_v_ _[n]_ _,_ (3)
_mχ_



_mχ_




- - _∞_
=



_dv f_ rel( _v_ ; _σ_ 1d) _[σ][T]_ [ (] _[v]_ [)]
0 _mχ_



and evaluate it numerically using either Gauss–Laguerre quadrature (for integrals over [0 _, ∞_ ))
or adaptive quadrature, with internal regression tests verifying agreement at the 10 _[−]_ [9] level for
representative cases.


**3.5** **Scattering rate and an illustrative** _r_ 1 **radius**


A commonly used halo-level diagnostic is the per-particle scattering rate,


Γ( _r_ ) = _[ρ]_ [(] _[r]_ [)] _⟨σT v⟩_ _,_ (4)

_mχ_


3


where _ρ_ ( _r_ ) is the local dark matter density, and the velocity moment depends on the assumed
velocity distribution. A simple core-formation proxy used in analytic SIDM treatments is the
radius _r_ 1 at which a typical particle has scattered once over a halo age _t_ age [4],


Γ( _r_ 1) _t_ age _≃_ 1 _._ (5)


`sidmkit` includes an illustrative implementation for NFW halos to support order-of-magnitude
estimates. We stress that this is _not_ a substitute for controlled SIDM simulations; it is best used
for exploration and unit/regression checks.

### 4 Rotation-curve fitting to SPARC rotmod files


**4.1** **SPARC** `rotmod` **format and baryonic decomposition**


SPARC provides rotation curves and baryonic decompositions for disk galaxies, including
contributions from gas, stellar disk, and (when applicable) bulge [6]. In the `rotmod` format used
here, each radial bin contains:


_

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04735.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---

## 10. First measurement of the Hubble constant from a combined weak lensing and gravitational-wave standard siren analysis

**Authors:** Felipe Andrade-Oliveira, David Sanchez-Cid, Danny Laghi, Marcelle Soares-Santos

**ArXiv ID:** 2601.04774 (2601.04774v1)

**Abstract:**
We present a new measurement of the Hubble constant ($H_0$) resulting from the first joint analysis of standard sirens with weak gravitational lensing and galaxy clustering observables comprising three two-point correlation functions (3$\times$2pt). For the 3$\times$2pt component of the analysis, we use data from the Dark Energy Survey (DES) Year 3 release. For the standard sirens component, we use data from the Gravitational-Wave Transient Catalog 4.0 released by the LIGO-Virgo-KAGRA (LVK) Collaboration. For GW170817, the only standard siren for which extensive electromagnetic follow-up observations exist, we also use measurements of the host galaxy redshift and inclination angle estimates derived from observations of a superluminal jet from its remnant. Our joint analysis yields $H_0 = 67.9^{+4.4}_{-4.3}$~km~s$^{-1}$~Mpc$^{-1}$, a $6.4\%$ measurement, while improving the DES constraint on the total abundance of matter $\Omega_m$ by $22\%$. Removing the jet information degrades the $H_0$ precision to $9.9\%$. The measurement of $H_0$ remains a central problem in cosmology with a multitude of approaches being vigorously pursued in the community aiming to reconcile significantly discrepant measurements at the percent-level. In light of the impending new data releases from DES and LVK, and anticipating much more constraining power from 3$\times$2pt observables using newly commissioned survey instruments, we demonstrate that incorporating standard sirens into the cosmology framework of large cosmic surveys is a viable route towards that goal.Authors' comments:5 pages, 2 figures

**Links:**
- [Abstract](https://arxiv.org/abs/2601.04774)
- [PDF](https://arxiv.org/pdf/2601.04774.pdf)

**Paper Content (Markdown):**

```markdown
_Astronomy & Astrophysics_ manuscript no. main ©ESO 2026
January 9, 2026


Letter to the Editor

## **First measurement of the Hubble constant from a combined weak** **lensing and gravitational-wave standard siren analysis**


Felipe Andrade-Oliveira [⋆], David Sanchez-Cid, Danny Laghi, and Marcelle Soares-Santos


Physik-Institut, Universität Zürich, Winterthurerstrasse 190, 8057 Zürich, Switzerland


Received January XX, 2026


**ABSTRACT**


We present a new measurement of the Hubble constant ( _H_ 0) resulting from the first joint analysis of standard sirens with weak gravitational lensing and galaxy clustering observables comprising three two-point correlation functions (3×2pt). For the 3×2pt component
of the analysis, we use data from the Dark Energy Survey (DES) Year 3 release. For the standard sirens component, we use data
from the Gravitational-Wave Transient Catalog 4.0 released by the LIGO-Virgo-KAGRA (LVK) Collaboration. For GW170817, the
only standard siren for which extensive electromagnetic follow-up observations exist, we also use measurements of the host galaxy
redshift and inclination angle estimates derived from observations of a superluminal jet from its remnant. Our joint analysis yields
_H_ 0 = 67.9 [+]  - [4] 4 [.] . [4] 3 [km s][−][1][ Mpc][−][1][, a 6][.][4% measurement, while improving the DES constraint on the total abundance of matter][ Ω] _[m]_ [ by 22%.]
Removing the jet information degrades the _H_ 0 precision to 9.9%. The measurement of _H_ 0 remains a central problem in cosmology
with a multitude of approaches being vigorously pursued in the community aiming to reconcile significantly discrepant measurements
at the percent-level. In light of the impending new data releases from DES and LVK, and anticipating much more constraining power
from 3×2pt observables using newly commissioned survey instruments, we demonstrate that incorporating standard sirens into the
cosmology framework of large cosmic surveys is a viable route towards that goal.


**Key words.** cosmological parameters – gravitational lensing: weak – gravitational waves



**1. Introduction**


The measurement of the present-day expansion rate, the Hubble constant ( _H_ 0), poses an empirical challenge to the ΛCDM
cosmological model. _H_ 0 values inferred from the early Universe through analyses of the cosmic microwave background
(CMB) data under the ΛCDM assumption (Aghanim et al. 2020;
Louis et al. 2025; Camphuis et al. 2025) are in significant (≳
5-σ) tension with direct measurements obtained from lateUniverse observables such as type Ia supernovae (SNe Ia) calibrated using the cosmic distance ladder (Riess et al. 2022).
A series of analyses on both the early- (Efstathiou & Gratton
2019; Hou et al. 2018) and late-time (Casertano et al. 2025;
Di Valentino & Brout 2024) sides have been carried out to reconcile these measurements. While those efforts have achieved
substantial progress in narrowing down the list of possible systematic effects, the problem persists.
Motivated by this scenario, we present a new measurement
of the Hubble constant resulting from an independent analysis
of multi-messenger observables. Our approach builds upon the
well-established multi-probe framework, known as the 3×2pt
analysis in the photometric survey community (Abbott et al.
2022; Heymans et al. 2021; Miyatake et al. 2023). This framework is mainly driven by the weak gravitational lensing, cosmic shear, 2-point correlation function (2PCF) (Secco et al.
2022; Amon et al. 2022; Wright et al. 2025), which is sensitive to the sum of baryonic and dark matter abundance (Ω _m_ )
and the amplitude of matter density fluctuations, combined
with galaxy clustering 2PCF (Rodríguez-Monroy et al. 2022)
and the cross-correlation of galaxy shear and galaxy posi

⋆ e-mail: `felipe.andradeoliveira@physik.uzh.ch`



tion fields (Prat et al. 2022; Pandey et al. 2022; Porredon et al.
2022). We add to the 3×2pt observables gravitational wave (GW)
distance indicators known as standard sirens (Holz & Hughes
2005), which are binary coalescence events used for ΛCDM
cosmological measurements (Abac et al. 2025b) with redshift
information gathered from electromagnetic (EM) counterpart observations (Abbott et al. 2017a), catalogues of likely
host galaxies (Soares-Santos et al. 2019; Abbott et al. 2021;
Finke et al. 2021; Palmese et al. 2023; Mastrogiovanni et al.
2023; Bom et al. 2024; Mukherjee et al. 2024; de Matos et al.
2025), and the mass spectrum of the binary population (Abbott et al. 2023; Karathanasis et al. 2023). As information from follow-up observations of the EM counterpart of the
standard siren GW170817 (Abbott et al. 2017b,c; Mooley et al.
2018) have been proven effective in enhancing its constraining
power for cosmology (Hotokezaka et al. 2019), we also incorporate such information.
Standard sirens and 3×2pt are of particular interest to the _H_ 0
problem because their observables are obtained without reliance
on the cosmic distance ladder. With this first combined measurement, we show that incorporating standard sirens into the multiprobe cosmology framework of large cosmic surveys is a viable
route to constrain _H_ 0 and thereby inform the ongoing debate.


**2. Data**


_2.1. DES Y3_


The DES is a _grizY_ photometric survey that mapped 5000 deg [2]
of the southern sky from Cerro Tololo, Chile, using the Dark
Energy Camera (DECam, Flaugher et al. (2015)) between 2013


Article number, page 1


_A&A proofs:_ manuscript no. main



and 2019. The DES Y3 data release includes the first three
years (Sevilla-Noarbe et al. 2021).
We use the data vectors published in Abbott et al. (2022) and
available at the DES Data Management Portal [1] . The weak lensing signal is extracted from a source galaxy sample drawn from a
galaxy shape catalogue (Gatti et al. 2021) comprising about 100
million galaxies. These are divided into four tomographic redshift bins extending to _z_ = 2, with a weighted effective source
density of _n_ eff = 5.9 galaxies per arcmin [2] and a shape noise of
σe = 0.26. Galaxy clustering is measured using the MagLim lens
galaxy sample (Porredon et al. 2021, 2022), which contains 10.7
million galaxies split into six redshift bins. Redshift distributions
for the source and lens samples are derived using self-organizing
maps (Giannini et al. 2024) and the Directional Neighbourhood
Fitting method (De Vicente et al. 2016), respectively.


_2.2. GWTC-4.0_


The LIGO-Virgo-KAGRA Collaboration (LVK) network of observatories (Abac et al. 2025a) consists of two Laser Interferometer Gravitational-Wave Observatory (LIGO; Aasi et al. 2015)
detectors in the USA plus Virgo (Acernese et al. 2015) in Europe
and KAGRA (Akutsu et al. 2021) in Japan. These four detectors are enhanced Michelson interferometers sensitive to gravitational waves in the ∼10-1000 Hz band (Abac et al. 2025a).
The LVK observing schedule is organized into observing runs
during which one or more detectors are operational. The fourth
Gravitational-Wave Transient Catalog (GWTC-4.0; Abac et al.
2025a,c,e) comprises GW transient candidates accumulated between the first observing run (O1) and the end of the first
part of the fourth observing run (O4a), which ended in January 2024. The catalogue reports the inferred source parameters under the hypothesis that these transients are caused by
GWs emitted by compact binary coalescences (CBCs). This
catalogue has been used to study the population properties of
CBCs (Abac et al. 2025d) and to constrain late-time cosmological parameters (Abac et al. 2025b).
We use data presented in Abac et al. (2025b) and available
in Zenodo [2] . We take the posterior samples for _H_ 0 and Ω _m_ obtained using 142 CBCs out of the 218 GW candidates included in
GWTC-4.0. We specifically choose the subset of the posteriors
corresponding to the spectral sirens analysis, which relies exclusively on the GW data and uses the mass spectrum as the source
of redshift information. GW170817 (Abbott et al. 2017b,c) is the
only GWTC-4.0 bright siren (i.e., a CBC with a confirmed EM
counterpart). To re-analyse GW170817 for this work, we also
use the injection files (Essick et al. 2025; Abac et al. 2025c) used
to correct for GW selection effects and the posterior samples for
all its CBC parameters, including the luminosity distance ( _dL_ )
and the source inclination angle (θ _JN_ ).


_2.3. GW170817 EM counterpart information_


Thanks to the discovery of its EM counterpart (Abbott et al.
2017c), a wealth of multi-messenger data on GW170817 is available. This allows us to supplement the GW data with information
derived from follow-up observations of the counterpart itself, as
well as with archival data such as the spectroscopic redshift of
the host galaxy, NGC 4993, and the velocity field at its position.
We use the host recession velocity _v_ = 3327 ± 72 km s [−][1]
(Crook et al. 2007) relative to the CMB and the radial peculiar


1 [https://des.ncsa.illinois.edu/releases/y3a2/Y3key-products](https://des.ncsa.illinois.edu/releases/y3a2/Y3key-products)
[2 https://doi.org/10.5281/zenodo.16919645 (Version v1)](https://doi.org/10.5281/zenodo.16919645)


Article number, page 2



velocity ⟨ _vp_ ⟩ = 310 ± 150 km s [−][1] (Carrick et al. 2015). We
also use inclination angle constraint, 15 [◦] < θ _jet_ < 29 [◦], obtained from observations of superluminal motion of the remnant’s jet between 75 and 230 days post-merger (Mooley et al.
2018; Hotokezaka et al. 2019).


**3. Methods**


_3.1. Weak lensing and galaxy clustering_


In the 3×2pt framework, cosmological information is inferred
from overdensity and shear fields constructed from observations of galaxy positions and shapes. Field-level information
is then compressed into the three 2PCFs, shear-shear, galaxygalaxy, and galaxy-shear, which in turn can be jointly compared to the cosmological model predictions (Krause et al. 2021;
Friedrich et al. 2021).
The theoretical framework is complemented with the modelling of known astrophys

... (truncated, full content available in Markdown file)
```

*Full Markdown file: /var/folders/cp/_9lpm9wx5fb6cs5ng7pf0nj80000gn/T/benty_arxiv_pdfs/2601.04774.md*

### Research Motivation

*To be filled by AI analysis*

### Methodology

*To be filled by AI analysis*

### Data Used

*To be filled by AI analysis*

### Conclusions

*To be filled by AI analysis*

---
