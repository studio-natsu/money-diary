import tkinter as tk
import tkinter.messagebox as mb
import csv
from datetime import date

root = tk.Tk()
root.title("家計簿")
root.geometry("450x500")
root.configure(bg='#efd7d9')

# 収入入力ラベル
tk.Label(root, text="収入", foreground='#8a2e36').grid(row=0, column=0, padx=5, pady=5)
income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1, padx=5, pady=5)

# 金額入力フォーム
tk.Label(root, text="金額", foreground='#8a2e36').grid(row=1, column=0, padx=5, pady=5)
income_amount_entry= tk.Entry(root)
income_amount_entry.grid(row=1, column=1, padx=5, pady=5)

# 登録ボタン
income_add_button = tk.Button(root, text="登録")
income_add_button.grid(row=2, column=1, padx=5, pady=5)


# 支出入力ラベル
tk.Label(root, text="支出", foreground='#8a2e36').grid(row=0, column=3, padx=5, pady=5)
expense_entry = tk.Entry(root)
expense_entry.grid(row=0, column=4, padx=5, pady=5)

# 金額入力フォーム
tk.Label(root, text="金額", foreground='#8a2e36').grid(row=1, column=3, padx=5, pady=5)
expense_amount_entry = tk.Entry(root)
expense_amount_entry.grid(row=1, column=4, padx=5, pady=5)

# 登録ボタン
expense_add_button = tk.Button(root, text="登録")
expense_add_button.grid(row=2, column=4, padx=5, pady=5)

# 支出一覧
table_frame = tk.Frame(root)
table_frame.grid(row=3, column=1, columnspan=4, padx=5, pady=5)
table = tk.Listbox(table_frame, width=60, height=10)
table.pack()

# 合計金額ラベル
total_label = tk.Label(root, text="残高: 0円", foreground='#ad3943', background = '#efd7d9')
total_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

"""

登録ボタンを押したときの処理。
add_income()とadd_expense()を定義し、入力された収入・収支を
CSVファイルに追加（作成）し、残高を更新していく関数。


"""
def add_income():
    income = income_entry.get() 
    amount1 = int(income_amount_entry.get()) #収入入力ラベルに入力された値を取得
    today = date.today().strftime("%Y/%m/%d")
    
    # 収入をファイルに追加（csvファイルの作成）
    with open("expenses.csv", "a", encoding='utf8') as f: 
        writer = csv.writer(f)
        writer.writerow([today, income, amount1 ])

    # 収支一覧に収入を追加(tk.ENDで文末へ)
    table.insert(tk.END, f"{today} {income} {amount1}円")

    # 残高の更新
    total = sum([int(table.get(i).split()[-1].replace("円", "")) for i in range(table.size())])
    total_label.configure(text=f"残高: {total}円")

    # 入力フォームをクリア
    income_entry.delete(0, tk.END)
    income_amount_entry.delete(0, tk.END)

income_add_button.configure(command=add_income)    
    
    
def add_expense():
    expense = expense_entry.get()
    amount2 = -int(expense_amount_entry.get())
    today = date.today().strftime("%Y/%m/%d")

    # 支出をファイルに追加
    with open("expenses.csv", "a", encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow([today, expense, amount2])

    # 収支一覧に支出を追加
    table.insert(tk.END, f"{today} {expense} {amount2}円",)

    # 残高の更新
    total = sum([int(table.get(i).split()[-1].replace("円", "")) for i in range(table.size())])
    total_label.configure(text=f"残高: {total}円")

    # 入力フォームをクリア
    expense_entry.delete(0, tk.END)
    expense_amount_entry.delete(0, tk.END)


expense_add_button.configure(command=add_expense,)

root.mainloop()