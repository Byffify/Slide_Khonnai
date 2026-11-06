# 3-minute version: selected TechBite slides as they are, with the original 5-member team slide from the Milestone 2 deck.
# Build: python build/build_deck.py pitch3  ->  khonnai-pitch-3min.html
import re

import slides_khonnai as m2
import slides_techbite as tb

OUT_NAME = 'khonnai-pitch-3min.html'
TITLE = 'Khonnai · Pitch 3 นาที'
BRAND = 'Group 3'
ASSETS = tb.ASSETS
TEAM = m2.TEAM  # photos: build/assets/team-1..5, the build's default prefix

team_slide = next(s for s in m2.SLIDES if '{TEAM}' in s)
cover = re.sub(r'<div class="abs in soft" style="left:150px;bottom:92px.*?</div>', '', tb.SLIDES[0], count=1, flags=re.S)  # no applicant/team block on the cover
problem = tb.SLIDES[1].replace('<i data-i="alert"></i><span><b>ข้อจำกัด</b>', '<i data-i="users"></i><span><b>Early Adopter</b>')
team = m2.SLIDES[m2.SLIDES.index(team_slide)]

# (slide, section name) in pitch order; section numbers follow this order
ORDER = [(cover.replace('ted_youth_startup_fund --kx-techbite', 'INT403 --pitch'), 'Khonnai'),
         (problem, 'Problem'),
         (tb.SLIDES[4], 'Technology'),
         (re.sub(r'data-cubes="[^"]*"', 'data-cubes="none"', tb.SLIDES[11], count=1), 'Traction'),
         (tb.SLIDES[3], 'Market'),
         (tb.SLIDES[7], 'Business Model'),
         (tb.SLIDES[6], 'Positioning'),
         (team, 'Team'),
         (tb.SLIDES[8], 'Funding'),
         (tb.SLIDES[18], 'Reference')]
NSEC = len(ORDER) - 1


def place(k, s, name):
    s = re.sub(r'data-sec="\d+"', f'data-sec="{k:02d}"', s, count=1)
    return re.sub(r'data-secname="[^"]*"', f'data-secname="{name}"', s, count=1)


SLIDES = [place(k, s, name) for k, (s, name) in enumerate(ORDER)]
