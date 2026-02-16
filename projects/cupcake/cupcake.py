import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QComboBox, QDoubleSpinBox,
    QDateEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QFrame
)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QColor


# ─────────────────────────────────────────────
#  This list is your "backend" / data store.
#  Every order is saved here as a dictionary.
# ─────────────────────────────────────────────
orders = []          # e.g. [{"cupcake": "Vanilla", "price": 3.50, "date": "2025-06-01"}, ...]


class CupcakeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧁 Cupcake Order App")
        self.setMinimumSize(600, 520)
        self.init_ui()

    # ── Build the entire UI ──────────────────
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(14)
        main_layout.setContentsMargins(24, 24, 24, 24)

        # ── Title ────────────────────────────
        title = QLabel("🧁 Cupcake Orders")
        title.setFont(QFont("Georgia", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # ── Divider ──────────────────────────
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        # ── Input area ───────────────────────
        form_layout = QHBoxLayout()
        form_layout.setSpacing(12)

        # 1. QComboBox – cupcake type
        col1 = QVBoxLayout()
        col1.addWidget(QLabel("Cupcake Type"))
        self.combo_cupcake = QComboBox()
        self.combo_cupcake.addItems(["Vanilla", "Chocolate", "Strawberry"])
        col1.addWidget(self.combo_cupcake)
        form_layout.addLayout(col1)

        # 2. QDoubleSpinBox – price per cupcake
        col2 = QVBoxLayout()
        col2.addWidget(QLabel("Price per Cupcake ($)"))
        self.spin_price = QDoubleSpinBox()
        self.spin_price.setRange(0.01, 999.99)   # min / max values
        self.spin_price.setSingleStep(0.50)       # arrow step
        self.spin_price.setDecimals(2)            # decimal places
        self.spin_price.setValue(3.50)            # default value
        self.spin_price.setPrefix("$ ")
        col2.addWidget(self.spin_price)
        form_layout.addLayout(col2)

        # 3. QDateEdit – order date
        col3 = QVBoxLayout()
        col3.addWidget(QLabel("Order Date"))
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)     # shows a calendar picker
        self.date_edit.setDate(QDate.currentDate())  # default = today
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        col3.addWidget(self.date_edit)
        form_layout.addLayout(col3)

        main_layout.addLayout(form_layout)

        # ── Order button ─────────────────────
        self.btn_order = QPushButton("Place Order")
        self.btn_order.setFixedHeight(40)
        self.btn_order.setFont(QFont("Arial", 11, QFont.Bold))
        self.btn_order.setStyleSheet(
            "QPushButton { background-color: #e07b54; color: white; border-radius: 8px; }"
            "QPushButton:hover { background-color: #c9623c; }"
            "QPushButton:pressed { background-color: #a84e30; }"
        )
        # Connect the button click to our handler function
        self.btn_order.clicked.connect(self.place_order)
        main_layout.addWidget(self.btn_order)

        # ── Divider ──────────────────────────
        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line2)

        # ── Orders label ─────────────────────
        orders_label = QLabel("Order History")
        orders_label.setFont(QFont("Georgia", 13, QFont.Bold))
        main_layout.addWidget(orders_label)

        # ── QTableWidget – displays the orders ──
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Cupcake Type", "Price", "Date"])

        # Make columns stretch to fill available width
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Disable editing cells by clicking on them
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Highlight the whole row when selected
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        main_layout.addWidget(self.table)

        # ── Summary label ────────────────────
        self.summary_label = QLabel("Total orders: 0  |  Total spent: $0.00")
        self.summary_label.setAlignment(Qt.AlignRight)
        self.summary_label.setStyleSheet("color: #555; font-style: italic;")
        main_layout.addWidget(self.summary_label)

    # ── Called every time "Place Order" is clicked ──
    def place_order(self):
        # 1. Read the current values from each widget
        cupcake = self.combo_cupcake.currentText()          # str
        price   = self.spin_price.value()                   # float
        date    = self.date_edit.date().toString("yyyy-MM-dd")  # str

        # 2. Build a dictionary for this order
        order = {
            "cupcake": cupcake,
            "price":   price,
            "date":    date,
        }

        # 3. Append it to the global list  ← this is your "backend" storage
        orders.append(order)

        # 4. Refresh the table and summary
        self.refresh_table()

    # ── Redraws the table from the `orders` list ──
    def refresh_table(self):
        self.table.setRowCount(len(orders))   # one row per order

        for row_index, order in enumerate(orders):
            # Create table items (cells)
            item_cupcake = QTableWidgetItem(order["cupcake"])
            item_price   = QTableWidgetItem(f'${order["price"]:.2f}')
            item_date    = QTableWidgetItem(order["date"])

            # Center-align the price and date cells
            item_price.setTextAlignment(Qt.AlignCenter)
            item_date.setTextAlignment(Qt.AlignCenter)

            # Alternate row colour for readability
            if row_index % 2 == 0:
                bg = QColor("#fff8f5")
            else:
                bg = QColor("#fdeee8")

            for item in (item_cupcake, item_price, item_date):
                item.setBackground(bg)

            # Place the items into the table
            self.table.setItem(row_index, 0, item_cupcake)
            self.table.setItem(row_index, 1, item_price)
            self.table.setItem(row_index, 2, item_date)

        # Update the summary line
        total_spent = sum(o["price"] for o in orders)
        self.summary_label.setText(
            f"Total orders: {len(orders)}  |  Total spent: ${total_spent:.2f}"
        )


# ── Entry point ─────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CupcakeApp()
    window.show()
    sys.exit(app.exec_())