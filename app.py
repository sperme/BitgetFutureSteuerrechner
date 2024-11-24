import pandas as pd
import requests
import customtkinter as ctk
from tkinter import filedialog, messagebox, Toplevel
from fpdf import FPDF
import logging

# Logging setup
logging.basicConfig(level=logging.ERROR, filename='app.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Wechselkurs-Funktion
def get_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json().get("rates", {})
        return rates.get("EUR", 1)  # Standardmäßig 1, falls EUR nicht gefunden wird
    except Exception as e:
        logging.error(f"Error fetching exchange rate: {e}")
        return 1

# Datenverarbeitung
def process_data(file_path, use_exchange_rate, include_church_tax, include_loss_carryover, currency):
    try:
        data = pd.read_csv(file_path)

        expected_columns = {'realized pnl', 'fees'}
        if not expected_columns.issubset(data.columns):
            raise ValueError("Die CSV-Datei enthält nicht die erwarteten Spalten: 'realized pnl' und 'fees'.")

        data['realized pnl'] = data['realized pnl'].replace({r'[^\d.-]': ''}, regex=True).astype(float)
        data['fees'] = data['fees'].replace({r'[^\d.-]': ''}, regex=True).astype(float)

        exchange_rate = get_exchange_rate() if use_exchange_rate else 1
        factor = exchange_rate if currency == "EUR" else 1 / exchange_rate

        total_gains = data[data['realized pnl'] > 0]['realized pnl'].sum() * factor
        total_losses = data[data['realized pnl'] < 0]['realized pnl'].sum() * factor
        total_fees = data['fees'].sum() * factor
        realized_pnl = total_gains + total_losses

        taxable_income = realized_pnl - total_fees
        if taxable_income < 0 and not include_loss_carryover:
            taxable_income = 0

        tax_rate = 0.25
        solidarity_surcharge = 0.055
        church_tax = 0.09 if include_church_tax else 0

        tax_due = taxable_income * (tax_rate + tax_rate * solidarity_surcharge + tax_rate * church_tax) if taxable_income > 0 else 0
        loss_carryover = abs(realized_pnl) if realized_pnl < 0 and include_loss_carryover else 0

        results = {
            "Realized PnL": f"{realized_pnl:.2f} {currency}",
            "Total Gains": f"{total_gains:.2f} {currency}",
            "Total Losses": f"{abs(total_losses):.2f} {currency}",
            "Total Fees": f"{total_fees:.2f} {currency}",
            "Taxable Income": f"{taxable_income:.2f} {currency}",
            "Tax Due": f"{tax_due:.2f} {currency}",
            "Loss Carryover": f"{loss_carryover:.2f} {currency}"
        }

        return results, data, exchange_rate

    except Exception as e:
        logging.error(f"Error processing data: {e}")
        messagebox.showerror("Fehler", f"Fehler bei der Datenverarbeitung: {e}")
        return None, None, None

# PDF-Export
def export_to_pdf(results, currency):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Helvetica", style="B", size=24)
    pdf.cell(0, 10, "Futures Steuerergebnisse", ln=True, align="C")
    pdf.ln(20)

    pdf.set_font("Helvetica", size=12)
    for key, value in results.items():
        pdf.cell(90, 10, key, border=1, align="L", ln=0)
        pdf.cell(90, 10, value, border=1, align="R", ln=1)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        pdf.output(save_path)
        messagebox.showinfo("Erfolg", f"PDF erfolgreich gespeichert unter {save_path}")

# Info-Popup
def show_info(message):
    info_window = Toplevel()
    info_window.title("Information")
    info_window.geometry("400x200")
    info_label = ctk.CTkLabel(info_window, text=message, wraplength=350, font=("Helvetica", 12))
    info_label.pack(pady=20, padx=20)

# GUI-Klasse
class FuturesTaxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Futures-Steuerrechner")
        self.root.geometry("900x700")

        self.currency = "EUR"
        self.file_path = None

        self.frame = ctk.CTkFrame(root, corner_radius=15)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text="Futures-Steuerrechner", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        self.create_controls()

        self.results_text = ctk.CTkTextbox(self.frame, width=400, height=200, corner_radius=15)
        self.results_text.pack(pady=20)

    def create_controls(self):
        # Dateiauswahl
        self.file_button_frame = ctk.CTkFrame(self.frame)
        self.file_button_frame.pack(pady=10)
        self.select_file_button = ctk.CTkButton(self.file_button_frame, text="CSV-Datei laden", command=self.load_csv)
        self.select_file_button.grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.file_button_frame, text="?", command=lambda: show_info(
            "Wählen Sie eine CSV-Datei mit den Spalten 'realized pnl' und 'fees', um mit der Berechnung zu beginnen."
        )).grid(row=0, column=1, padx=5)

        # Steueroptionen
        self.include_church_tax_var = ctk.IntVar(value=0)
        self.include_loss_carryover_var = ctk.IntVar(value=0)
        self.use_exchange_rate_var = ctk.IntVar(value=1)

        self.include_church_tax_checkbox = ctk.CTkCheckBox(
            self.frame, text="Kirchensteuer einbeziehen", variable=self.include_church_tax_var,
            command=self.update_results
        )
        self.include_church_tax_checkbox.pack(pady=5)
        ctk.CTkButton(self.frame, text="?", command=lambda: show_info(
            "Wenn diese Option aktiviert ist, wird ein Kirchensteuersatz von 9% auf die Steuer angerechnet."
        )).pack(pady=5)

        self.include_loss_carryover_checkbox = ctk.CTkCheckBox(
            self.frame, text="Verlustvortrag einbeziehen", variable=self.include_loss_carryover_var,
            command=self.update_results
        )
        self.include_loss_carryover_checkbox.pack(pady=5)
        ctk.CTkButton(self.frame, text="?", command=lambda: show_info(
            "Aktivieren Sie diese Option, um Verluste in zukünftige Steuerperioden zu übertragen."
        )).pack(pady=5)

        self.use_exchange_rate_checkbox = ctk.CTkCheckBox(
            self.frame, text="Wechselkurs anwenden", variable=self.use_exchange_rate_var,
            command=self.update_results
        )
        self.use_exchange_rate_checkbox.pack(pady=5)
        ctk.CTkButton(self.frame, text="?", command=lambda: show_info(
            "Wenn aktiviert, wird der aktuelle Wechselkurs zwischen USD und EUR verwendet."
        )).pack(pady=5)

        # PDF-Export
        self.export_button = ctk.CTkButton(self.frame, text="Export als PDF", command=self.export_results)
        self.export_button.pack(pady=10)

    def load_csv(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.update_results()

    def update_results(self):
        if self.file_path:
            self.results, self.data, self.exchange_rate = process_data(
                self.file_path,
                self.use_exchange_rate_var.get(),
                self.include_church_tax_var.get(),
                self.include_loss_carryover_var.get(),
                self.currency
            )
            if self.results:
                self.results_text.delete("0.0", "end")
                for key, value in self.results.items():
                    self.results_text.insert("end", f"{key}: {value}\n")

    def export_results(self):
        if hasattr(self, 'results'):
            export_to_pdf(self.results, self.currency)

# Anwendung starten
if __name__ == "__main__":
    root = ctk.CTk()
    app = FuturesTaxApp(root)
    root.mainloop()
