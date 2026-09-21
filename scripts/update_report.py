#!/usr/bin/env python3
"""Rebuild LifelinkAI project report front pages + snapshot images."""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
import pymupdf as fitz

ROOT = Path("/Users/gulabchaudhari/Downloads/PredictiX-main")
SRC = Path(
    "/Users/gulabchaudhari/.cursor/projects/Users-gulabchaudhari-Downloads-PredictiX-main/attachments/f6bdbab0-5cf3-4b96-82d8-c599d469a6c1/PREDICTIX_REPORT__1_.pdf"
)
OUT = ROOT / "PREDICTIX REPORT.pdf"
OUT_ALT = ROOT / "LifelinkAI_REPORT.pdf"
COLLEGE_LOGO = ROOT / "assets/ABES_logo.jpg"
APP_LOGO = ROOT / "Frontend/src/assets/LifelinkAI_logo.jpg"
SHOTS = ROOT / "Screenshots"
TMP = ROOT / ".report_preview" / "front_pages.pdf"
COLLEGE = "ABES Engineering College"
COLLEGE_CODE = "College Code 032"
DEPT = "Department of Computer Science and Engineering (Data Science)"

MEMBERS = [
    {
        "name": "Hariom Tiwari",
        "admission": "2023B0131070",
        "enrollment": "2300320130111",
        "section": "ITA",
        "branch": "CSE (Data Science)",
        "email": "hariompstiwari@gmail.com",
        "mobile": "8840392421",
    },
    {
        "name": "Amit Pal",
        "admission": "2023B0131097",
        "enrollment": "2300320130038",
        "section": "ITC",
        "branch": "CSE (Data Science)",
        "email": "amit9696680583@gmail.com",
        "mobile": "9696680583",
    },
    {
        "name": "Aakash Singh",
        "admission": "2023B0131207",
        "enrollment": "2300320130001",
        "section": "ITC",
        "branch": "CSE (Data Science)",
        "email": "akash936924@gmail.com",
        "mobile": "9369243876",
    },
    {
        "name": "Tushar",
        "admission": "2023B0131219",
        "enrollment": "2300320130259",
        "section": "ITC",
        "branch": "CSE (Data Science)",
        "email": "sg6006694@gmail.com",
        "mobile": "9548596633",
    },
]


def styles():
    base = getSampleStyleSheet()
    return {
        "center": ParagraphStyle(
            "c", parent=base["Normal"], alignment=TA_CENTER, fontName="Times-Roman", fontSize=12, leading=16
        ),
        "centerBold": ParagraphStyle(
            "cb", parent=base["Normal"], alignment=TA_CENTER, fontName="Times-Bold", fontSize=12, leading=16
        ),
        "title": ParagraphStyle(
            "t", parent=base["Normal"], alignment=TA_CENTER, fontName="Times-Bold", fontSize=16, leading=20
        ),
        "h1": ParagraphStyle(
            "h1", parent=base["Normal"], alignment=TA_CENTER, fontName="Times-Bold", fontSize=18, leading=22
        ),
        "body": ParagraphStyle(
            "b", parent=base["Normal"], alignment=TA_JUSTIFY, fontName="Times-Roman", fontSize=11, leading=15
        ),
        "left": ParagraphStyle(
            "l", parent=base["Normal"], alignment=TA_LEFT, fontName="Times-Roman", fontSize=11, leading=14
        ),
        "small": ParagraphStyle(
            "s", parent=base["Normal"], alignment=TA_CENTER, fontName="Times-Roman", fontSize=10, leading=13
        ),
        "member": ParagraphStyle(
            "m", parent=base["Normal"], alignment=TA_LEFT, fontName="Times-Roman", fontSize=10, leading=13
        ),
        "memberName": ParagraphStyle(
            "mn", parent=base["Normal"], alignment=TA_LEFT, fontName="Times-Bold", fontSize=11, leading=14
        ),
    }


def build_front_pages(path: Path):
    s = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
    )
    story = []

    # ---- PAGE 1: Cover ----
    if COLLEGE_LOGO.exists():
        college_img = Image(str(COLLEGE_LOGO), width=3.4 * inch, height=1.35 * inch)
        college_img.hAlign = "CENTER"
        story.append(college_img)
        story.append(Spacer(1, 6))
        story.append(Paragraph(COLLEGE, s["centerBold"]))
        story.append(Paragraph(COLLEGE_CODE, s["small"]))
        story.append(Spacer(1, 10))

    story.append(Paragraph("Project Report On", s["center"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("LIFELINKAI — A MULTI DISEASE PREDICTOR", s["title"]))
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "A dissertation submitted in partial fulfilment of the requirements of "
            "Bachelor of Technology Degree in Computer Science and Engineering "
            "(Data Science).",
            s["small"],
        )
    )
    story.append(Spacer(1, 10))
    if APP_LOGO.exists():
        img = Image(str(APP_LOGO), width=1.1 * inch, height=1.1 * inch)
        img.hAlign = "CENTER"
        story.append(img)
    story.append(Spacer(1, 10))
    story.append(Paragraph("Submitted by / Group Members", s["centerBold"]))
    story.append(Spacer(1, 6))

    for i, m in enumerate(MEMBERS, 1):
        story.append(Paragraph(f"{i}. {m['name']}", s["memberName"]))
        story.append(
            Paragraph(
                f"Admission No.: {m['admission']}&nbsp;&nbsp;|&nbsp;&nbsp;"
                f"Enrollment No.: {m['enrollment']}<br/>"
                f"Section: {m['section']}&nbsp;&nbsp;|&nbsp;&nbsp;"
                f"Branch: {m['branch']}<br/>"
                f"Email: {m['email']}&nbsp;&nbsp;|&nbsp;&nbsp;"
                f"Mobile: {m['mobile']}",
                s["member"],
            )
        )
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph(DEPT, s["centerBold"]))
    story.append(Paragraph(COLLEGE, s["centerBold"]))
    story.append(Paragraph("Ghaziabad, Uttar Pradesh", s["center"]))

    # ---- PAGE 2: Certificate ----
    from reportlab.platypus import PageBreak

    story.append(PageBreak())
    story.append(Paragraph("CERTIFICATE OF APPROVAL", s["h1"]))
    story.append(Spacer(1, 16))
    names = ", ".join(m["name"] for m in MEMBERS)
    story.append(
        Paragraph(
            f"This is to certify that this report of the B. Tech. project, entitled "
            f"<b>LifelinkAI — A Multi Disease Predictor</b>, is a record of bona-fide work "
            f"carried out by <b>{names}</b> under the supervision and guidance of the "
            f"undersigned faculty mentor at <b>{COLLEGE}</b> ({COLLEGE_CODE}).",
            s["body"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "In our opinion, the report in its present form is in partial fulfilment of "
            "the requirements of the Bachelor of Technology program in Computer Science "
            "and Engineering (Data Science). To the best of our knowledge, the results "
            "embodied in this report are original in nature and worthy of incorporation "
            "in the present version of the report.",
            s["body"],
        )
    )
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "It is understood that by this approval the undersigned does not necessarily "
            "endorse or approve any statement made, opinion expressed, or conclusion "
            "drawn therein, but approve this thesis for the purpose for which it is "
            "submitted.",
            s["body"],
        )
    )
    story.append(Spacer(1, 28))
    story.append(Paragraph("Group Members", s["centerBold"]))
    story.append(Spacer(1, 8))
    rows = [["Name", "Admission No.", "Enrollment No.", "Section"]]
    for m in MEMBERS:
        rows.append([m["name"], m["admission"], m["enrollment"], m["section"]])
    table = Table(rows, colWidths=[140, 110, 130, 60])
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.93, 0.98)),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 36))
    story.append(
        Paragraph(
            "Guide / Supervisor ____________________ &nbsp;&nbsp;&nbsp;&nbsp; "
            "Head of the Department ____________________",
            s["small"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph(DEPT, s["small"]))
    story.append(Paragraph(f"{COLLEGE} ({COLLEGE_CODE})", s["small"]))

    # ---- PAGE 3: Acknowledgement ----
    story.append(PageBreak())
    story.append(Paragraph("ACKNOWLEDGEMENT", s["h1"]))
    story.append(Spacer(1, 14))
    story.append(
        Paragraph(
            "We sincerely extend our heartfelt gratitude to our faculty mentor for "
            "invaluable guidance, insightful suggestions, and unwavering support "
            "throughout this project. Their expertise and encouragement have been "
            "instrumental in shaping our work and helping us overcome challenges.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "We are also deeply grateful to ABES Engineering College and the faculty of "
            "the Computer Science and Engineering (Data Science) department for providing "
            "us with the resources, knowledge, and opportunities that enabled us to "
            "pursue this project successfully.",
            s["body"],
        )
    )
    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Additionally, we would like to express our appreciation to our peers and "
            "families for their thoughtful feedback, constant encouragement, and "
            "motivation. This project is a culmination of the collective support we "
            "received from everyone around us.",
            s["body"],
        )
    )
    story.append(Spacer(1, 22))
    for m in MEMBERS:
        story.append(
            Paragraph(
                f"<b>{m['name']}</b>: _______________________<br/>"
                f"Admission No. – {m['admission']}<br/>"
                f"Enrollment No. – {m['enrollment']}",
                s["left"],
            )
        )
        story.append(Spacer(1, 10))

    doc.build(story)


def replace_snapshot_images(doc: fitz.Document):
    mapping = {
        33: (SHOTS / "SS1.png",),  # home
        34: (SHOTS / "SS2.png", SHOTS / "SS2.png"),  # signup/login -> login shots
        35: (SHOTS / "SS3.png",),  # predictors
        45: (SHOTS / "SS4.png",),  # about
    }
    for page_index, files in mapping.items():
        page = doc[page_index]
        infos = page.get_image_info(xrefs=True)
        for info, file in zip(infos, files):
            xref = info["xref"]
            if file.exists():
                page.replace_image(xref, filename=str(file))
                print(f"Replaced image on page {page_index + 1} xref={xref} <- {file.name}")


def soft_text_updates(doc: fitz.Document):
    """Update visible PredictiX captions on snapshot pages where possible."""
    replacements = [
        ("Predictix", "LifelinkAI"),
        ("PredictiX", "LifelinkAI"),
        ("PREDICTIX", "LIFELINKAI"),
    ]
    # Focus on snapshot / abstract / conclusion pages
    for i in list(range(3, 6)) + list(range(33, 47)):
        if i >= len(doc):
            continue
        page = doc[i]
        for old, new in replacements:
            hits = page.search_for(old)
            for rect in hits:
                # white-out then rewrite
                page.add_redact_annot(rect, fill=(1, 1, 1))
            if hits:
                page.apply_redactions()
                for rect in hits:
                    # slightly enlarge for longer name
                    page.insert_textbox(
                        rect + (0, -1, 40, 2),
                        new,
                        fontname="times-roman",
                        fontsize=9,
                        color=(0, 0, 0),
                        align=1,
                    )


def main():
    TMP.parent.mkdir(exist_ok=True)
    build_front_pages(TMP)
    print("Built front pages:", TMP)

    front = fitz.open(TMP)
    doc = fitz.open(SRC)

    # Replace first 3 pages
    doc.delete_pages(0, 2)
    doc.insert_pdf(front, start_at=0)
    front.close()

    replace_snapshot_images(doc)
    soft_text_updates(doc)

    doc.save(OUT, garbage=4, deflate=True)
    doc.save(OUT_ALT, garbage=4, deflate=True)
    doc.close()
    print("Saved:", OUT)
    print("Saved:", OUT_ALT)


if __name__ == "__main__":
    main()
