from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_passbook_pdf(user):
    filename = f"PassBooks/{user.name}_Passbook.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(180, 800, "BOI DIGITAL PASSBOOK")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Account Holder: {user.name}")
    c.drawString(50, 750, f"Account No: {user.hide_acc}")
    c.drawString(50, 730, f"Current Balance: Rs. {user.balance}")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 690, "DATE & TIME")
    c.drawString(180, 690, "TYPE")
    c.drawString(360, 690, "AMOUNT")
    c.drawString(460, 690, "BALANCE")

    y = 670
    c.setFont("Helvetica", 10)

    for item in user.history:
        try:
            if "|" in item and len(item.split("|")) == 4:
                dt, t_type, amt, bal = item.split("|")
                c.drawString(50, y, dt)
                c.drawString(180, y, t_type[:22])
                c.drawString(360, y, amt.replace("₹", "Rs. "))
                c.drawString(460, y, bal.replace("₹", "Rs. "))
            else:
                c.drawString(50, y, item[:95])

            y -= 20

            if y < 50:
                c.showPage()
                y = 800
                c.setFont("Helvetica", 10)

        except Exception:
            pass

    c.save()
    return filename