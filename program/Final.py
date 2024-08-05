from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ___________________________________________________________
container = Tk()
container.iconbitmap('Images/icon.ico')
container.title('Fast Food Ordering System')
container.geometry('1150x650')
container.resizable(False, False)

# ___________________________________________________________
def btnQty(tmp00):

	if tmpo == 1:
		EntTtl.insert(0, 0)
		txtLst = "Yumberger"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(39)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 2:
		EntTtl.insert(0, 0)
		txtLst = "1 - pc. Chickenjoy w/ jolly Spaghetti"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(109)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 3:
		EntTtl.insert(0, 0)
		txtLst = "1 - pc. Chickenjoy"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(84)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 4:
		EntTtl.insert(0, 0)
		txtLst = "jolly Spaghetti"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(55)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 5:
		EntTtl.insert(0, 0)
		txtLst = "1 - pc. CJ w/ BSteak and Half JS Super Meal"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(182)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 6:
		EntTtl.insert(0, 0)
		txtLst = "2 - pc. Chickenjoy"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(168)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 7:
		EntTtl.insert(0, 0)
		txtLst = "Cheesy Yumberger"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(54)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 8:
		EntTtl.insert(0, 0)
		txtLst = "Buko Pie"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(36)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 9 or tmpo == 32:
		EntTtl.insert(0, 0)
		txtLst = "Champ and Joy Super Meal"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(264)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 10:
		EntTtl.insert(0, 0)
		txtLst = "Crisscut Fries"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(72)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 11:
		EntTtl.insert(0, 0)
		txtLst = "Choco Hazelnut Sundae"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(50)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 12:
		EntTtl.insert(0, 0)
		txtLst = "Honey Beef Rice Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(164)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 13:
		EntTtl.insert(0, 0)
		txtLst = "Tuna Pie"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(50)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 14:
		EntTtl.insert(0, 0)
		txtLst = "Garlic Pepper Marinated Chicken"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(165)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 15 or tmpo == 24:
		EntTtl.insert(0, 0)
		txtLst = "4 - pc. Cj family Box w/ Large Fries"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(402)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 16 or tmpo == 25:
		EntTtl.insert(0, 0)
		txtLst = "4 - pc. Cj Family Box Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(297)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 17 or tmpo == 26:
		EntTtl.insert(0, 0)
		txtLst = "6 - pc. Chickenjoy Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(439)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 18 or tmpo == 27:
		EntTtl.insert(0, 0)
		txtLst = "8 - pc. Chickenjoy Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(549)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 19:
		EntTtl.insert(0, 0)
		txtLst = "Crisscut Fries Bucket"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(274)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 20:
		EntTtl.insert(0, 0)
		txtLst = "1 - pc.Breakfast Chickenjoy"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(105)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 21:
		EntTtl.insert(0, 0)
		txtLst = "Beef Tapa"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(121)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 22:
		EntTtl.insert(0, 0)
		txtLst = "Corned Beef"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(121)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 23:
		EntTtl.insert(0, 0)
		txtLst = "Longganisa"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(121)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 28:
		EntTtl.insert(0, 0)
		txtLst = "2 - pc. Sweet Chili Chicken w/ Drink"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(219)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 29:
		EntTtl.insert(0, 0)
		txtLst = "2 - pc. Sweet Chili Chicken Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(193)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 30:
		EntTtl.insert(0, 0)
		txtLst = "4 - pc. Sweet Chili Chicken Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(352)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 31:
		EntTtl.insert(0, 0)
		txtLst = "6 - pc. Sweet Chili Chicken Solo"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(523)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 33:
		EntTtl.insert(0, 0)
		txtLst = "Champ Knock-out Deal"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(264)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 34:
		EntTtl.insert(0, 0)
		txtLst = "Spicy Champ Jr."
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(87)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	elif tmpo == 35:
		EntTtl.insert(0, 0)
		txtLst = "Spicy Champ"
		ottal = float(EntTtl.get())
		EntTtl.delete(0, END)
		EntQty.delete(0, END)
		EntQty.insert(0, tmp00)
		total = float(tmp00) * float(193)
		ottal += total
		EntTtl.insert(0, ottal)
		print(ottal, total)
		ordLst = str(tmp00) + " pc/s. " + txtLst + " for P" + str(total) + "\n"
		txtlft.insert(1.0, ordLst)
		stcDec(tmpo)
	else:
		messagebox.showinfo("Notice", "Unexpected Error Occured")

def stcDec(tmpVar):
	if tmpVar == 1:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 2:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 3:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 4:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 5:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 6:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 7:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 8:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 9 or tmpVar == 32:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 10:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 11:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 12:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 13:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 14:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 15 or tmpVar == 24:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 16 or tmpVar == 25:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 17 or tmpVar == 26:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 18 or tmpVar == 27:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 19:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 20:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 21:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 22:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 23:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 28:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 29:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 30:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 31:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 33:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 34:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	elif tmpVar == 35:
		stocks = EntStc.get()
		qntity = EntQty.get()
		EntStc.delete(0, END)
		nwstck = int(stocks) - int(qntity)
		EntStc.insert(0, nwstck)
	else:
		messagebox.showinfo("Notice", "Error Occured")
	deduct(tmpVar)

# ___________________________________________________________
def btnOrd(tmp00):
	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()
	cursr.execute("SELECT *, oid FROM tblStocks WHERE oid=1")
	crrnt = cursr.fetchall()

	global tmpo
	tmpo = tmp00

	EntQty.delete(0, END)
	EntStc.delete(0, END)

	if tmp00 == 1:
		for record in crrnt:
			EntStc.insert(0, record[0])
	elif tmp00 == 2:
		for record in crrnt:
			EntStc.insert(0, record[1])
	elif tmp00 == 3:
		for record in crrnt:
			EntStc.insert(0, record[2])
	elif tmp00 == 4:
		for record in crrnt:
			EntStc.insert(0, record[3])
	elif tmp00 == 5:
		for record in crrnt:
			EntStc.insert(0, record[4])
	elif tmp00 == 6:
		for record in crrnt:
			EntStc.insert(0, record[5])
	elif tmp00 == 7:
		for record in crrnt:
			EntStc.insert(0, record[6])
	elif tmp00 == 8:
		for record in crrnt:
			EntStc.insert(0, record[7])
	elif tmp00 == 9 or tmp00 == 32:
		for record in crrnt:
			EntStc.insert(0, record[8])
	elif tmp00 == 10:
		for record in crrnt:
			EntStc.insert(0, record[9])
	elif tmp00 == 11:
		for record in crrnt:
			EntStc.insert(0, record[10])
	elif tmp00 == 12:
		for record in crrnt:
			EntStc.insert(0, record[11])
	elif tmp00 == 13:
		for record in crrnt:
			EntStc.insert(0, record[12])
	elif tmp00 == 14:
		for record in crrnt:
			EntStc.insert(0, record[13])
	elif tmp00 == 15 or tmp00 == 24:
		for record in crrnt:
			EntStc.insert(0, record[14])
	elif tmp00 == 16 or tmp00 == 25:
		for record in crrnt:
			EntStc.insert(0, record[15])
	elif tmp00 == 17 or tmp00 == 26:
		for record in crrnt:
			EntStc.insert(0, record[16])
	elif tmp00 == 18 or tmp00 == 27:
		for record in crrnt:
			EntStc.insert(0, record[17])
	elif tmp00 == 19:
		for record in crrnt:
			EntStc.insert(0, record[18])
	elif tmp00 == 20:
		for record in crrnt:
			EntStc.insert(0, record[19])
	elif tmp00 == 21:
		for record in crrnt:
			EntStc.insert(0, record[20])
	elif tmp00 == 22:
		for record in crrnt:
			EntStc.insert(0, record[21])
	elif tmp00 == 23:
		for record in crrnt:
			EntStc.insert(0, record[22])
	elif tmp00 == 28:
		for record in crrnt:
			EntStc.insert(0, record[23])
	elif tmp00 == 29:
		for record in crrnt:
			EntStc.insert(0, record[24])
	elif tmp00 == 30:
		for record in crrnt:
			EntStc.insert(0, record[25])
	elif tmp00 == 31:
		for record in crrnt:
			EntStc.insert(0, record[26])
	elif tmp00 == 33:
		for record in crrnt:
			EntStc.insert(0, record[27])
	elif tmp00 == 34:
		for record in crrnt:
			EntStc.insert(0, record[28])
	elif tmp00 == 35:
		for record in crrnt:
			EntStc.insert(0, record[29])
	else:
		messagebox.showinfo("Notice", "Error Occured")

	cnnct.commit()
	cnnct.close()


def Stocks():
	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	cursr.execute("SELECT *, oid FROM tblStocks WHERE oid=1")
	crrnt = cursr.fetchall()

	global stck01
	global stck02
	global stck03
	global stck04
	global stck05
	global stck06
	global stck07
	global stck08
	global stck09
	global stck10
	global stck11
	global stck12
	global stck13
	global stck14
	global stck15
	global stck16
	global stck17
	global stck18
	global stck19
	global stck20
	global stck21
	global stck22
	global stck23
	global stck24
	global stck25
	global stck26
	global stck27
	global stck28
	global stck29
	global stck30

	for record in crrnt:
		stck01 = record[0]
		stck02 = record[1]
		stck03 = record[2]
		stck04 = record[3]
		stck05 = record[4]
		stck06 = record[5]
		stck07 = record[6]
		stck08 = record[7]
		stck09 = record[8]
		stck10 = record[9]
		stck11 = record[10]
		stck12 = record[11]
		stck13 = record[12]
		stck14 = record[13]
		stck15 = record[14]
		stck16 = record[15]
		stck17 = record[16]
		stck18 = record[17]
		stck19 = record[18]
		stck20 = record[19]
		stck21 = record[20]
		stck22 = record[21]
		stck23 = record[22]
		stck24 = record[23]
		stck25 = record[24]
		stck26 = record[25]
		stck27 = record[26]
		stck28 = record[27]
		stck29 = record[28]
		stck30 = record[29]

	cnnct.commit()
	cnnct.close()

Stocks()

def backup():
	EntStc.delete(0, END)
	EntTtl.delete(0, END)
	EntQty.delete(0, END)
	txtlft.delete(1.0, END)

	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	cursr.execute("""UPDATE tblStocks SET
		attr01 = :attr01,
		attr02 = :attr02,
		attr03 = :attr03,
		attr04 = :attr04,
		attr05 = :attr05,
		attr06 = :attr06,
		attr07 = :attr07,
		attr08 = :attr08,
		attr09 = :attr09,
		attr10 = :attr10,
		attr11 = :attr11,
		attr12 = :attr12,
		attr13 = :attr13,
		attr14 = :attr14,
		attr15 = :attr15,
		attr16 = :attr16,
		attr17 = :attr17,
		attr18 = :attr18,
		attr19 = :attr19,
		attr20 = :attr20,
		attr21 = :attr21,
		attr22 = :attr22,
		attr23 = :attr23,
		attr24 = :attr24,
		attr25 = :attr25,
		attr26 = :attr26,
		attr27 = :attr27,
		attr28 = :attr28,
		attr29 = :attr29,
		attr30 = :attr30

		WHERE oid=1""",
		{
		'attr01' : stck01,
		'attr02' : stck02,
		'attr03' : stck03,
		'attr04' : stck04,
		'attr05' : stck05,
		'attr06' : stck06,
		'attr07' : stck07,
		'attr08' : stck08,
		'attr09' : stck09,
		'attr10' : stck10,
		'attr11' : stck11,
		'attr12' : stck12,
		'attr13' : stck13,
		'attr14' : stck14,
		'attr15' : stck15,
		'attr16' : stck16,
		'attr17' : stck17,
		'attr18' : stck18,
		'attr19' : stck19,
		'attr20' : stck20,
		'attr21' : stck21,
		'attr22' : stck22,
		'attr23' : stck23,
		'attr24' : stck24,
		'attr25' : stck25,
		'attr26' : stck26,
		'attr27' : stck27,
		'attr28' : stck28,
		'attr29' : stck29,
		'attr30' : stck30		
		})

	cnnct.commit()
	cnnct.close()

def plcOrd():
	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	crrnt = EntTtl.get()
	if crrnt != "":
		cursr.execute("INSERT INTO tblOrderList VALUES (:total, :lists)",
		{
		'total': EntTtl.get(),
		'lists': txtlft.get("1.0", "end - 1l")
		})
		
		messagebox.showinfo('Notice', 'Transactions were saved successfully')
		txtlft.delete(1.0, END)
		EntTtl.delete(0, END)
		Stocks()
		fClear()
	else:
		messagebox.showinfo('Notice', 'Error Occured, Please try again later.')

	cnnct.commit()
	cnnct.close()

def fClear():

	EntQty.delete(0, END)
	EntStc.delete(0, END)

def deduct(tmpvar):
	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	if tmpvar == 1:
		cursr.execute("""UPDATE tblStocks SET
			attr01 = :attr01
			WHERE oid = 1""",
			{
			'attr01': int(EntStc.get())
			})
	elif tmpvar == 2:
		cursr.execute("""UPDATE tblStocks SET
			attr02 = :attr02
			WHERE oid = 1""",
			{
			'attr02': int(EntStc.get())
			})
	elif tmpvar == 3:
		cursr.execute("""UPDATE tblStocks SET
			attr03 = :attr03
			WHERE oid = 1""",
			{
			'attr03': int(EntStc.get())
			})
	elif tmpvar == 4:
		cursr.execute("""UPDATE tblStocks SET
			attr04 = :attr04
			WHERE oid = 1""",
			{
			'attr04': int(EntStc.get())
			})
	elif tmpvar == 5:
		cursr.execute("""UPDATE tblStocks SET
			attr05 = :attr05
			WHERE oid = 1""",
			{
			'attr05': int(EntStc.get())
			})
	elif tmpvar == 6:
		cursr.execute("""UPDATE tblStocks SET
			attr06 = :attr06
			WHERE oid = 1""",
			{
			'attr06': int(EntStc.get())
			})
	elif tmpvar == 7:
		cursr.execute("""UPDATE tblStocks SET
			attr07 = :attr07
			WHERE oid = 1""",
			{
			'attr07': int(EntStc.get())
			})
	elif tmpvar == 8:
		cursr.execute("""UPDATE tblStocks SET
			attr08 = :attr08
			WHERE oid = 1""",
			{
			'attr08': int(EntStc.get())
			})
	elif tmpvar == 9 or tmpvar == 32:
		cursr.execute("""UPDATE tblStocks SET
			attr09 = :attr09
			WHERE oid = 1""",
			{
			'attr09': int(EntStc.get())
			})
	elif tmpvar == 10:
		cursr.execute("""UPDATE tblStocks SET
			attr10 = :attr10
			WHERE oid = 1""",
			{
			'attr10': int(EntStc.get())
			})
	elif tmpvar == 11:
		cursr.execute("""UPDATE tblStocks SET
			attr11 = :attr11
			WHERE oid = 1""",
			{
			'attr11': int(EntStc.get())
			})
	elif tmpvar == 12:
		cursr.execute("""UPDATE tblStocks SET
			attr12 = :attr12
			WHERE oid = 1""",
			{
			'attr12': int(EntStc.get())
			})
	elif tmpvar == 13:
		cursr.execute("""UPDATE tblStocks SET
			attr13 = :attr13
			WHERE oid = 1""",
			{
			'attr13': int(EntStc.get())
			})
	elif tmpvar == 14:
		cursr.execute("""UPDATE tblStocks SET
			attr14 = :attr14
			WHERE oid = 1""",
			{
			'attr14': int(EntStc.get())
			})
	elif tmpvar == 15 or tmpvar == 24:
		cursr.execute("""UPDATE tblStocks SET
			attr15 = :attr15
			WHERE oid = 1""",
			{
			'attr15': int(EntStc.get())
			})
	elif tmpvar == 16 or tmpvar == 25:
		cursr.execute("""UPDATE tblStocks SET
			attr16 = :attr16
			WHERE oid = 1""",
			{
			'attr16': int(EntStc.get())
			})
	elif tmpvar == 17 or tmpvar == 26:
		cursr.execute("""UPDATE tblStocks SET
			attr17 = :attr17
			WHERE oid = 1""",
			{
			'attr17': int(EntStc.get())
			})
	elif tmpvar == 18 or tmpvar == 27:
		cursr.execute("""UPDATE tblStocks SET
			attr18 = :attr18
			WHERE oid = 1""",
			{
			'attr18': int(EntStc.get())
			})
	elif tmpvar == 19:
		cursr.execute("""UPDATE tblStocks SET
			attr19 = :attr19
			WHERE oid = 1""",
			{
			'attr19': int(EntStc.get())
			})
	elif tmpvar == 20:
		cursr.execute("""UPDATE tblStocks SET
			attr20 = :attr20
			WHERE oid = 1""",
			{
			'attr20': int(EntStc.get())
			})
	elif tmpvar == 21:
		cursr.execute("""UPDATE tblStocks SET
			attr21 = :attr21
			WHERE oid = 1""",
			{
			'attr21': int(EntStc.get())
			})
	elif tmpvar == 22:
		cursr.execute("""UPDATE tblStocks SET
			attr22 = :attr22
			WHERE oid = 1""",
			{
			'attr22': int(EntStc.get())
			})
	elif tmpvar == 23:
		cursr.execute("""UPDATE tblStocks SET
			attr23 = :attr23
			WHERE oid = 1""",
			{
			'attr23': int(EntStc.get())
			})
	elif tmpvar == 28:
		cursr.execute("""UPDATE tblStocks SET
			attr24 = :attr24
			WHERE oid = 1""",
			{
			'attr24': int(EntStc.get())
			})
	elif tmpvar == 29:
		cursr.execute("""UPDATE tblStocks SET
			attr25 = :attr25
			WHERE oid = 1""",
			{
			'attr25': int(EntStc.get())
			})
	elif tmpvar == 30:
		cursr.execute("""UPDATE tblStocks SET
			attr26 = :attr26
			WHERE oid = 1""",
			{
			'attr26': int(EntStc.get())
			})
	elif tmpvar == 31:
		cursr.execute("""UPDATE tblStocks SET
			attr27 = :attr27
			WHERE oid = 1""",
			{
			'attr27': int(EntStc.get())
			})
	elif tmpvar == 33:
		cursr.execute("""UPDATE tblStocks SET
			attr28 = :attr28
			WHERE oid = 1""",
			{
			'attr28': int(EntStc.get())
			})
	elif tmpvar == 34:
		cursr.execute("""UPDATE tblStocks SET
			attr29 = :attr29
			WHERE oid = 1""",
			{
			'attr29': int(EntStc.get())
			})
	elif tmpvar == 35:
		cursr.execute("""UPDATE tblStocks SET
			attr30 = :attr30
			WHERE oid = 1""",
			{
			'attr30': int(EntStc.get())
			})
	else:
		messagebox.showinfo("Notice", "Error Occured")

	cnnct.commit()
	cnnct.close()

def mgStck():
	container.withdraw()

	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	cursr.execute("SELECT *, oid FROM tblStocks WHERE oid=1")
	crrnt = cursr.fetchall()

	global con_02

	con_02 = Tk()
	con_02.title('Manage Stocks')
	con_02.geometry('1200x450')
	con_02.iconbitmap('Images/icon.ico')
	con_02.resizable(False, False)


	global ent001
	global ent002
	global ent003
	global ent004
	global ent005
	global ent006
	global ent007
	global ent008
	global ent009
	global ent010
	global ent011
	global ent012
	global ent013
	global ent014
	global ent015
	global ent016
	global ent017
	global ent018
	global ent019
	global ent020
	global ent021
	global ent022
	global ent023
	global ent024
	global ent025
	global ent026
	global ent027
	global ent028
	global ent029
	global ent030

	prvt_01 = LabelFrame(con_02, width=1150, height=600, bg="white", pady=10)
	lbl_ttl = Label(con_02, text="Manage Stock Inventory", font='arial 30 bold', bg="black", fg="white").place(x=45, y=20)
	btn_fcs = Button(con_02, text="Save Changes", relief=RIDGE, bg="#ff0021", fg="white", command=svChng).place(x=1067, y=45)
	btn_cnl = Button(con_02, text="Cancel", relief=RIDGE, bg="#ff781f", fg="white", command=lambda: hnseek(2)).place(x=1015, y=45)
	
	cvs_ms = Canvas(prvt_01, width=750, height=250, bg="white")
	scr_ms = ttk.Scrollbar(prvt_01, orient=HORIZONTAL, command=cvs_ms.xview)
	cvs_ms.configure(xscrollcommand=scr_ms.set, highlightthickness=0)
	pvt_01 = Frame(cvs_ms, bg="white")
	cvs_ms.create_window((0, 0), window=pvt_01, anchor="nw")
	
	prvt_02 = LabelFrame(con_02, width=350, height=150, bg="white", pady=10)
	lbl_mng = Label(con_02, text="Remove Stocks  ", font='arial 30 bold', bg="black", fg="white").place(x=830, y=80)
	
	for i in range(7):
		row_i = i + 1
		lblcmp = "lbl_00" + str(i)
		lblcmp = Label(pvt_01, bg="white", text='000'+str(row_i), font='times 10 bold').grid(row=row_i, column=0, padx=(20, 0))

	nlbl01 = Label(pvt_01, bg="white", text='0008', font='times 10 bold').grid(row=1, column=6, padx=(40, 0))
	nlbl02 = Label(pvt_01, bg="white", text='0009', font='times 10 bold').grid(row=2, column=6, padx=(40, 0))
	nlbl03 = Label(pvt_01, bg="white", text='0014', font='times 10 bold').grid(row=1, column=11, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0028', font='times 10 bold').grid(row=1, column=31, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0029', font='times 10 bold').grid(row=2, column=31, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0030', font='times 10 bold').grid(row=3, column=31, padx=(40, 0))
	
	for i in range(4):
		row_i = i + 10
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+3, column=6, padx=(40, 0))

	for i in range(5):
		row_i = i + 15
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=16, padx=(40, 0))

	for i in range(4):
		row_i = i + 20
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=21, padx=(40, 0))

	for i in range(4):
		row_i = i + 24
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=26, padx=(40, 0))


	mlbl01 = Label(pvt_01, bg="white", text='Best Sellers', font='times 10 bold').grid(row=0, column=0, columnspan=2, sticky=W, padx=(20, 0))
	lbl001 = Label(pvt_01, text="Yumberger").grid(row=1, column=1, sticky=W)
	lbl002 = Label(pvt_01, text="1 - pc. Chickenjoy w/ JollySpag").grid(row=2, column=1, sticky=W)
	lbl003 = Label(pvt_01, text="1 - pc. Chickenjoy").grid(row=3, column=1, sticky=W)
	lbl004 = Label(pvt_01, text="Jolly Spaghetti").grid(row=4, column=1, sticky=W)
	lbl005 = Label(pvt_01, text="1 - pc. Cj w/ B Steak and Half Js S Meal").grid(row=5, column=1, sticky=W)
	lbl006 = Label(pvt_01, text="2 - pc. Chickenjoy").grid(row=6, column=1, sticky=W)
	lbl007 = Label(pvt_01, text="Cheesy Yumberger").grid(row=7, column=1, sticky=W)

	mlbl02 = Label(pvt_01, bg="white", text='New Products', font='times 10 bold').grid(row=0, column=6, columnspan=2, sticky=W, padx=(40, 0))
	lbl008 = Label(pvt_01, text="Buko Pie").grid(row=1, column=7, sticky=W)
	lbl009 = Label(pvt_01, text="Champ and Joy Super Meal").grid(row=2, column=7, sticky=W)
	lbl010 = Label(pvt_01, text="Crisscut Fries").grid(row=3, column=7, sticky=W)
	lbl011 = Label(pvt_01, text="Choco Hazelnut Sundae").grid(row=4, column=7, sticky=W)
	lbl012 = Label(pvt_01, text="Honey Beef Rice Solo").grid(row=5, column=7, sticky=W)
	lbl013 = Label(pvt_01, text="tuna Pie").grid(row=6, column=7, sticky=W)

	mlbl03 = Label(pvt_01, bg="white", text='Ready to Cook', font='times 10 bold').grid(row=0, columnspan=2, column=11, sticky=W, padx=(40, 0))
	lbl014 = Label(pvt_01, text="Garlic Pepper marinated Chicken").grid(row=1, column=12, sticky=W)
	
	mlbl04 = Label(pvt_01, bg="white", text='Family Meals', font='times 10 bold').grid(row=0, column=16, columnspan=2, sticky=W, padx=(40, 0))
	lbl015 = Label(pvt_01, text="4 - pc. Chickenjoy Family Box w/ Large Fries").grid(row=1, column=17)
	lbl016 = Label(pvt_01, text="4 - pc. Chickenjoy Family Box Solo").grid(row=2, column=17, sticky=W)
	lbl017 = Label(pvt_01, text="6 - pc. Chickenjoy Solo").grid(row=3, column=17, sticky=W)
	lbl018 = Label(pvt_01, text="8 - pc. Chickenjoy Solo").grid(row=4, column=17, sticky=W)
	lbl019 = Label(pvt_01, text="Crisscut Fries Bucket").grid(row=5, column=17, sticky=W)

	mlbl05 = Label(pvt_01, bg="white", text='Breakfast', font='times 10 bold').grid(row=0, column=21, columnspan=2, sticky=W, padx=(40, 0))
	lbl020 = Label(pvt_01, text="1 - pc. Breakfast Chickenjoy").grid(row=1, column=22, sticky=W)
	lbl021 = Label(pvt_01, text="Beef Tapa").grid(row=2, column=22, sticky=W)
	lbl022 = Label(pvt_01, text="Corned Beef").grid(row=3, column=22, sticky=W)
	lbl023 = Label(pvt_01, text="Longganisa").grid(row=4, column=22, sticky=W)
	
	mlbl06 = Label(pvt_01, bg="white", text='Sweet Chili Chicken', font='times 10 bold').grid(row=0, column=26, columnspan=2, sticky=W, padx=(40, 0))
	lbl024 = Label(pvt_01, text="2 - pc. Sweet Chili Chicken w/ Drink").grid(row=1, column=27, sticky=W)
	lbl025 = Label(pvt_01, text="2 - pc. Sweet Chili Chicken Solo").grid(row=2, column=27, sticky=W)
	lbl026 = Label(pvt_01, text="4 - pc. Sweet Chili Chicken Solo").grid(row=3, column=27, sticky=W)
	lbl027 = Label(pvt_01, text="6 - pc. Sweet Chili Chicken Solo").grid(row=4, column=27, sticky=W)
	
	mlbl06 = Label(pvt_01, bg="white", text='Burgers', font='times 10 bold').grid(row=0, column=31, columnspan=2, sticky=W, padx=(40, 0))
	lbl028 = Label(pvt_01, text="Champ Knock-out Deal").grid(row=1, column=32, sticky=W)
	lbl029 = Label(pvt_01, text="Spicy Champ Jr.").grid(row=2, column=32, sticky=W)
	lbl030 = Label(pvt_01, text="Spicy Champ").grid(row=3, column=32, sticky=W)
	
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(1, ent001.get())).grid(row=1, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(2, ent002.get())).grid(row=2, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(3, ent003.get())).grid(row=3, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(4, ent004.get())).grid(row=4, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(5, ent005.get())).grid(row=5, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(6, ent006.get())).grid(row=6, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(7, ent007.get())).grid(row=7, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(8, ent008.get())).grid(row=1, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(9, ent009.get())).grid(row=2, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(10, ent010.get())).grid(row=3, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(11, ent011.get())).grid(row=4, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(12, ent012.get())).grid(row=5, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(13, ent013.get())).grid(row=6, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(14, ent014.get())).grid(row=1, column=13, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(15, ent015.get())).grid(row=1, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(16, ent016.get())).grid(row=2, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(17, ent017.get())).grid(row=3, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(18, ent018.get())).grid(row=4, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(19, ent019.get())).grid(row=5, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(20, ent020.get())).grid(row=1, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(21, ent021.get())).grid(row=2, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(22, ent022.get())).grid(row=3, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(23, ent023.get())).grid(row=4, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(24, ent024.get())).grid(row=1, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(25, ent025.get())).grid(row=2, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(26, ent026.get())).grid(row=3, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(27, ent027.get())).grid(row=4, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(28, ent028.get())).grid(row=1, column=33, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(29, ent029.get())).grid(row=2, column=33, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", padx=5, command=lambda: subbtn(30, ent030.get())).grid(row=3, column=33, pady=(0, 2), padx=2)
	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(1, ent001.get())).grid(row=1, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(2, ent002.get())).grid(row=2, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(3, ent003.get())).grid(row=3, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(4, ent004.get())).grid(row=4, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(5, ent005.get())).grid(row=5, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(6, ent006.get())).grid(row=6, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(7, ent007.get())).grid(row=7, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(8, ent008.get())).grid(row=1, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(9, ent009.get())).grid(row=2, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(10, ent010.get())).grid(row=3, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(11, ent011.get())).grid(row=4, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(12, ent012.get())).grid(row=5, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(13, ent013.get())).grid(row=6, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(14, ent014.get())).grid(row=1, column=15, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(15, ent015.get())).grid(row=1, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(16, ent016.get())).grid(row=2, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(17, ent017.get())).grid(row=3, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(18, ent018.get())).grid(row=4, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(19, ent019.get())).grid(row=5, column=20, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(20, ent020.get())).grid(row=1, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(21, ent021.get())).grid(row=2, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(22, ent022.get())).grid(row=3, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(23, ent023.get())).grid(row=4, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(24, ent024.get())).grid(row=1, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(25, ent025.get())).grid(row=2, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(26, ent026.get())).grid(row=3, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(27, ent027.get())).grid(row=4, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(28, ent028.get())).grid(row=1, column=35, pady=(0, 2), padx=(2, 20))	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(29, ent029.get())).grid(row=2, column=35, pady=(0, 2), padx=(2, 20))	
	btn002 = Button(pvt_01, text="+", padx=5, command=lambda: addbtn(30, ent030.get())).grid(row=3, column=35, pady=(0, 2), padx=(2, 20))	

	ent001 = Entry(pvt_01, width=5)
	ent002 = Entry(pvt_01, width=5)
	ent003 = Entry(pvt_01, width=5)
	ent004 = Entry(pvt_01, width=5)
	ent005 = Entry(pvt_01, width=5)
	ent006 = Entry(pvt_01, width=5)
	ent007 = Entry(pvt_01, width=5)
	ent008 = Entry(pvt_01, width=5)
	ent009 = Entry(pvt_01, width=5)
	ent010 = Entry(pvt_01, width=5)
	ent011 = Entry(pvt_01, width=5)
	ent012 = Entry(pvt_01, width=5)
	ent013 = Entry(pvt_01, width=5)
	ent014 = Entry(pvt_01, width=5)
	ent015 = Entry(pvt_01, width=5)
	ent016 = Entry(pvt_01, width=5)
	ent017 = Entry(pvt_01, width=5)
	ent018 = Entry(pvt_01, width=5)
	ent019 = Entry(pvt_01, width=5)
	ent020 = Entry(pvt_01, width=5)
	ent021 = Entry(pvt_01, width=5)
	ent022 = Entry(pvt_01, width=5)
	ent023 = Entry(pvt_01, width=5)
	ent024 = Entry(pvt_01, width=5)
	ent025 = Entry(pvt_01, width=5)
	ent026 = Entry(pvt_01, width=5)
	ent027 = Entry(pvt_01, width=5)
	ent028 = Entry(pvt_01, width=5)
	ent029 = Entry(pvt_01, width=5)
	ent030 = Entry(pvt_01, width=5)

	ent001.grid(row=1, column=4)
	ent002.grid(row=2, column=4)
	ent003.grid(row=3, column=4)
	ent004.grid(row=4, column=4)
	ent005.grid(row=5, column=4)
	ent006.grid(row=6, column=4)
	ent007.grid(row=7, column=4)
	ent008.grid(row=1, column=9)
	ent009.grid(row=2, column=9)
	ent010.grid(row=3, column=9)
	ent011.grid(row=4, column=9)
	ent012.grid(row=5, column=9)
	ent013.grid(row=6, column=9)
	ent014.grid(row=1, column=14)
	ent015.grid(row=1, column=19)
	ent016.grid(row=2, column=19)
	ent017.grid(row=3, column=19)
	ent018.grid(row=4, column=19)
	ent019.grid(row=5, column=19)
	ent020.grid(row=1, column=24)
	ent021.grid(row=2, column=24)
	ent022.grid(row=3, column=24)
	ent023.grid(row=4, column=24)
	ent024.grid(row=1, column=29)
	ent025.grid(row=2, column=29)
	ent026.grid(row=3, column=29)
	ent027.grid(row=4, column=29)
	ent028.grid(row=1, column=34)
	ent029.grid(row=2, column=34)
	ent030.grid(row=3, column=34)

	for record in crrnt:
		ent001.insert(0, record[0]) 
		ent002.insert(0, record[1]) 
		ent003.insert(0, record[2]) 
		ent004.insert(0, record[3]) 
		ent005.insert(0, record[4]) 
		ent006.insert(0, record[5]) 
		ent007.insert(0, record[6]) 
		ent008.insert(0, record[7]) 
		ent009.insert(0, record[8]) 
		ent010.insert(0, record[9]) 
		ent011.insert(0, record[10]) 
		ent012.insert(0, record[11]) 
		ent013.insert(0, record[12]) 
		ent014.insert(0, record[13]) 
		ent015.insert(0, record[14]) 
		ent016.insert(0, record[15]) 
		ent017.insert(0, record[16]) 
		ent018.insert(0, record[17]) 
		ent019.insert(0, record[18]) 
		ent020.insert(0, record[19]) 
		ent021.insert(0, record[20]) 
		ent022.insert(0, record[21]) 
		ent023.insert(0, record[22]) 
		ent024.insert(0, record[23]) 
		ent025.insert(0, record[24]) 
		ent026.insert(0, record[25]) 
		ent027.insert(0, record[26]) 
		ent028.insert(0, record[27]) 
		ent029.insert(0, record[28]) 
		ent030.insert(0, record[29]) 
		
	cvs_ms.grid(row=0, column=0)
	scr_ms.place(x=0, y=242, width=750)
	cvs_ms.configure(xscrollcommand=scr_ms.set)
	cvs_ms.bind('<Configure>', lambda e: cvs_ms.configure(scrollregion=cvs_ms.bbox("all")))

	global DelQty
	global DelEnt

	lblDel = Label(prvt_02, text="Specify Stocks ID", font='times 10 bold').grid(row=0, column=0, padx=(20, 0), pady=3)
	DelQt1 = Label(prvt_02, text="Quantity", font='times 10 bold').grid(row=1, column=0, pady=3)
	DelEnt = Entry(prvt_02)
	DelQty = Entry(prvt_02)
	AllBtn = Button(prvt_02, text="All", relief=RIDGE, padx=10, command=lambda: clckal(DelEnt.get()))
	DelBtn = Button(prvt_02, text="Remove", relief=RIDGE, fg="white", bg="#ff0021", command=lambda: remstc(DelEnt.get()))
	
	DelBtn.grid(row=2, column=1, sticky=W+E, columnspan=2, padx=(5, 10), pady=(3, 103))
	AllBtn.grid(row=1, column=2, padx=(5, 10), pady=3)
	DelEnt.grid(row=0, column=1, columnspan=2, sticky=W+E, padx=(5, 10), pady=3)
	DelQty.grid(row=1, column=1, padx=(5, 10), pady=3)

	prvt_01.place(x=45, y=80)
	prvt_02.place(x=830, y=140)

	cnnct.commit()
	cnnct.close()

def vwStck():
	container.withdraw()

	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()
	cursr.execute("SELECT *, oid FROM tblStocks WHERE oid=1")
	crrnt = cursr.fetchall()

	global con_01

	con_01 = Tk()
	con_01.title('View Stocks')
	con_01.geometry('1200x450')
	con_01.iconbitmap('Images/icon.ico')
	con_01.resizable(False, False)

	prvt_01 = LabelFrame(con_01, width=1150, height=300, bg="white", pady=10)
	lbl_ttl = Label(con_01, text="Manage Stock Inventory", font='arial 30 bold', bg="black", fg="white").place(x=45, y=20)
	btn_cnl = Button(con_01, text="Cancel", relief=RIDGE, bg="#ff781f", fg="white", command=lambda: hnseek(1)).place(x=1100, y=45)
	
	cvs_ms = Canvas(prvt_01, width=1100, height=250, bg="white")
	scr_ms = ttk.Scrollbar(prvt_01, orient=HORIZONTAL, command=cvs_ms.xview)
	cvs_ms.configure(xscrollcommand=scr_ms.set, highlightthickness=0)
	pvt_01 = Frame(cvs_ms, bg="white")
	cvs_ms.create_window((0, 0), window=pvt_01, anchor="nw")
		
	for i in range(7):
		row_i = i + 1
		lblcmp = "lbl_00" + str(i)
		lblcmp = Label(pvt_01, bg="white", text='000'+str(row_i), font='times 10 bold').grid(row=row_i, column=0, padx=(20, 0))

	nlbl01 = Label(pvt_01, bg="white", text='0008', font='times 10 bold').grid(row=1, column=6, padx=(40, 0))
	nlbl02 = Label(pvt_01, bg="white", text='0009', font='times 10 bold').grid(row=2, column=6, padx=(40, 0))
	nlbl03 = Label(pvt_01, bg="white", text='0014', font='times 10 bold').grid(row=1, column=11, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0028', font='times 10 bold').grid(row=1, column=31, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0029', font='times 10 bold').grid(row=2, column=31, padx=(40, 0))
	nlbl04 = Label(pvt_01, bg="white", text='0030', font='times 10 bold').grid(row=3, column=31, padx=(40, 0))
	
	for i in range(4):
		row_i = i + 10
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+3, column=6, padx=(40, 0))

	for i in range(5):
		row_i = i + 15
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=16, padx=(40, 0))

	for i in range(4):
		row_i = i + 20
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=21, padx=(40, 0))

	for i in range(4):
		row_i = i + 24
		lblcmp = "lbl_00" + str(row_i)
		lblcmp = Label(pvt_01, bg="white", text='00'+str(row_i), font='times 10 bold').grid(row=i+1, column=26, padx=(40, 0))


	mlbl01 = Label(pvt_01, bg="white", text='Best Sellers', font='times 10 bold').grid(row=0, column=0, columnspan=2, sticky=W, padx=(20, 0))
	lbl001 = Label(pvt_01, text="Yumberger").grid(row=1, column=1, sticky=W)
	lbl002 = Label(pvt_01, text="1 - pc. Chickenjoy w/ JollySpag").grid(row=2, column=1, sticky=W)
	lbl003 = Label(pvt_01, text="1 - pc. Chickenjoy").grid(row=3, column=1, sticky=W)
	lbl004 = Label(pvt_01, text="Jolly Spaghetti").grid(row=4, column=1, sticky=W)
	lbl005 = Label(pvt_01, text="1 - pc. Cj w/ B Steak and Half Js S Meal").grid(row=5, column=1, sticky=W)
	lbl006 = Label(pvt_01, text="2 - pc. Chickenjoy").grid(row=6, column=1, sticky=W)
	lbl007 = Label(pvt_01, text="Cheesy Yumberger").grid(row=7, column=1, sticky=W)

	mlbl02 = Label(pvt_01, bg="white", text='New Products', font='times 10 bold').grid(row=0, column=6, columnspan=2, sticky=W, padx=(40, 0))
	lbl008 = Label(pvt_01, text="Buko Pie").grid(row=1, column=7, sticky=W)
	lbl009 = Label(pvt_01, text="Champ and Joy Super Meal").grid(row=2, column=7, sticky=W)
	lbl010 = Label(pvt_01, text="Crisscut Fries").grid(row=3, column=7, sticky=W)
	lbl011 = Label(pvt_01, text="Choco Hazelnut Sundae").grid(row=4, column=7, sticky=W)
	lbl012 = Label(pvt_01, text="Honey Beef Rice Solo").grid(row=5, column=7, sticky=W)
	lbl013 = Label(pvt_01, text="tuna Pie").grid(row=6, column=7, sticky=W)

	mlbl03 = Label(pvt_01, bg="white", text='Ready to Cook', font='times 10 bold').grid(row=0, columnspan=2, column=11, sticky=W, padx=(40, 0))
	lbl014 = Label(pvt_01, text="Garlic Pepper marinated Chicken").grid(row=1, column=12, sticky=W)
	
	mlbl04 = Label(pvt_01, bg="white", text='Family Meals', font='times 10 bold').grid(row=0, column=16, columnspan=2, sticky=W, padx=(40, 0))
	lbl015 = Label(pvt_01, text="4 - pc. Chickenjoy Family Box w/ Large Fries").grid(row=1, column=17)
	lbl016 = Label(pvt_01, text="4 - pc. Chickenjoy Family Box Solo").grid(row=2, column=17, sticky=W)
	lbl017 = Label(pvt_01, text="6 - pc. Chickenjoy Solo").grid(row=3, column=17, sticky=W)
	lbl018 = Label(pvt_01, text="8 - pc. Chickenjoy Solo").grid(row=4, column=17, sticky=W)
	lbl019 = Label(pvt_01, text="Crisscut Fries Bucket").grid(row=5, column=17, sticky=W)

	mlbl05 = Label(pvt_01, bg="white", text='Breakfast', font='times 10 bold').grid(row=0, column=21, columnspan=2, sticky=W, padx=(40, 0))
	lbl020 = Label(pvt_01, text="1 - pc. Breakfast Chickenjoy").grid(row=1, column=22, sticky=W)
	lbl021 = Label(pvt_01, text="Beef Tapa").grid(row=2, column=22, sticky=W)
	lbl022 = Label(pvt_01, text="Corned Beef").grid(row=3, column=22, sticky=W)
	lbl023 = Label(pvt_01, text="Longganisa").grid(row=4, column=22, sticky=W)
	
	mlbl06 = Label(pvt_01, bg="white", text='Sweet Chili Chicken', font='times 10 bold').grid(row=0, column=26, columnspan=2, sticky=W, padx=(40, 0))
	lbl024 = Label(pvt_01, text="2 - pc. Sweet Chili Chicken w/ Drink").grid(row=1, column=27, sticky=W)
	lbl025 = Label(pvt_01, text="2 - pc. Sweet Chili Chicken Solo").grid(row=2, column=27, sticky=W)
	lbl026 = Label(pvt_01, text="4 - pc. Sweet Chili Chicken Solo").grid(row=3, column=27, sticky=W)
	lbl027 = Label(pvt_01, text="6 - pc. Sweet Chili Chicken Solo").grid(row=4, column=27, sticky=W)
	
	mlbl06 = Label(pvt_01, bg="white", text='Burgers', font='times 10 bold').grid(row=0, column=31, columnspan=2, sticky=W, padx=(40, 0))
	lbl028 = Label(pvt_01, text="Champ Knock-out Deal").grid(row=1, column=32, sticky=W)
	lbl029 = Label(pvt_01, text="Spicy Champ Jr.").grid(row=2, column=32, sticky=W)
	lbl030 = Label(pvt_01, text="Spicy Champ").grid(row=3, column=32, sticky=W)
	
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=4, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=5, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=6, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=7, column=2, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=4, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=5, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=6, column=8, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=13, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=4, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=5, column=18, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=4, column=23, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=4, column=28, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=1, column=33, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=2, column=33, pady=(0, 2), padx=2)
	btn001 = Button(pvt_01, text="-", state=DISABLED, padx=5).grid(row=3, column=33, pady=(0, 2), padx=2)
	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=4, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=5, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=6, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=7, column=5, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=4, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=5, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=6, column=10, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=15, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=4, column=20, pady=(0, 2), padx=2)
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=5, column=20, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=4, column=25, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=4, column=30, pady=(0, 2), padx=2)	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=1, column=35, pady=(0, 2), padx=(2, 20))	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=2, column=35, pady=(0, 2), padx=(2, 20))	
	btn002 = Button(pvt_01, text="+", state=DISABLED, padx=5).grid(row=3, column=35, pady=(0, 2), padx=(2, 20))	

	ent001 = Entry(pvt_01, width=5)
	ent002 = Entry(pvt_01, width=5)
	ent003 = Entry(pvt_01, width=5)
	ent004 = Entry(pvt_01, width=5)
	ent005 = Entry(pvt_01, width=5)
	ent006 = Entry(pvt_01, width=5)
	ent007 = Entry(pvt_01, width=5)
	ent008 = Entry(pvt_01, width=5)
	ent009 = Entry(pvt_01, width=5)
	ent010 = Entry(pvt_01, width=5)
	ent011 = Entry(pvt_01, width=5)
	ent012 = Entry(pvt_01, width=5)
	ent013 = Entry(pvt_01, width=5)
	ent014 = Entry(pvt_01, width=5)
	ent015 = Entry(pvt_01, width=5)
	ent016 = Entry(pvt_01, width=5)
	ent017 = Entry(pvt_01, width=5)
	ent018 = Entry(pvt_01, width=5)
	ent019 = Entry(pvt_01, width=5)
	ent020 = Entry(pvt_01, width=5)
	ent021 = Entry(pvt_01, width=5)
	ent022 = Entry(pvt_01, width=5)
	ent023 = Entry(pvt_01, width=5)
	ent024 = Entry(pvt_01, width=5)
	ent025 = Entry(pvt_01, width=5)
	ent026 = Entry(pvt_01, width=5)
	ent027 = Entry(pvt_01, width=5)
	ent028 = Entry(pvt_01, width=5)
	ent029 = Entry(pvt_01, width=5)
	ent030 = Entry(pvt_01, width=5)

	ent001.grid(row=1, column=4)
	ent002.grid(row=2, column=4)
	ent003.grid(row=3, column=4)
	ent004.grid(row=4, column=4)
	ent005.grid(row=5, column=4)
	ent006.grid(row=6, column=4)
	ent007.grid(row=7, column=4)
	ent008.grid(row=1, column=9)
	ent009.grid(row=2, column=9)
	ent010.grid(row=3, column=9)
	ent011.grid(row=4, column=9)
	ent012.grid(row=5, column=9)
	ent013.grid(row=6, column=9)
	ent014.grid(row=1, column=14)
	ent015.grid(row=1, column=19)
	ent016.grid(row=2, column=19)
	ent017.grid(row=3, column=19)
	ent018.grid(row=4, column=19)
	ent019.grid(row=5, column=19)
	ent020.grid(row=1, column=24)
	ent021.grid(row=2, column=24)
	ent022.grid(row=3, column=24)
	ent023.grid(row=4, column=24)
	ent024.grid(row=1, column=29)
	ent025.grid(row=2, column=29)
	ent026.grid(row=3, column=29)
	ent027.grid(row=4, column=29)
	ent028.grid(row=1, column=34)
	ent029.grid(row=2, column=34)
	ent030.grid(row=3, column=34)

	for record in crrnt:
		ent001.insert(0, record[0]) 
		ent002.insert(0, record[1]) 
		ent003.insert(0, record[2]) 
		ent004.insert(0, record[3]) 
		ent005.insert(0, record[4]) 
		ent006.insert(0, record[5]) 
		ent007.insert(0, record[6]) 
		ent008.insert(0, record[7]) 
		ent009.insert(0, record[8]) 
		ent010.insert(0, record[9]) 
		ent011.insert(0, record[10]) 
		ent012.insert(0, record[11]) 
		ent013.insert(0, record[12]) 
		ent014.insert(0, record[13]) 
		ent015.insert(0, record[14]) 
		ent016.insert(0, record[15]) 
		ent017.insert(0, record[16]) 
		ent018.insert(0, record[17]) 
		ent019.insert(0, record[18]) 
		ent020.insert(0, record[19]) 
		ent021.insert(0, record[20]) 
		ent022.insert(0, record[21]) 
		ent023.insert(0, record[22]) 
		ent024.insert(0, record[23]) 
		ent025.insert(0, record[24]) 
		ent026.insert(0, record[25]) 
		ent027.insert(0, record[26]) 
		ent028.insert(0, record[27]) 
		ent029.insert(0, record[28]) 
		ent030.insert(0, record[29]) 
		
	cvs_ms.grid(row=0, column=0)
	scr_ms.place(x=0, y=242, width=1100)
	cvs_ms.configure(xscrollcommand=scr_ms.set)
	cvs_ms.bind('<Configure>', lambda e: cvs_ms.configure(scrollregion=cvs_ms.bbox("all")))

	prvt_01.pack(pady=75)

	cnnct.commit()
	cnnct.close()

def clckal(tempa):
	if DelEnt.get() == "":
		messagebox.showinfo("Notice", "Please specify the ID")
	else:
		if tempa == "0001":
			DelQty.delete(0, END)
			allTtl = ent001.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0002":
			DelQty.delete(0, END)
			allTtl = ent002.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0003":
			DelQty.delete(0, END)
			allTtl = ent003.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0004":
			DelQty.delete(0, END)
			allTtl = ent004.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0005":
			DelQty.delete(0, END)
			allTtl = ent005.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0006":
			DelQty.delete(0, END)
			allTtl = ent006.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0007":
			DelQty.delete(0, END)
			allTtl = ent007.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0008":
			DelQty.delete(0, END)
			allTtl = ent008.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0009":
			DelQty.delete(0, END)
			allTtl = ent009.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0010":
			DelQty.delete(0, END)
			allTtl = ent010.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0011":
			DelQty.delete(0, END)
			allTtl = ent011.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0012":
			DelQty.delete(0, END)
			allTtl = ent012.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0013":
			DelQty.delete(0, END)
			allTtl = ent013.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0014":
			DelQty.delete(0, END)
			allTtl = ent014.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0015":
			DelQty.delete(0, END)
			allTtl = ent015.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0016":
			DelQty.delete(0, END)
			allTtl = ent016.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0017":
			DelQty.delete(0, END)
			allTtl = ent017.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0018":
			DelQty.delete(0, END)
			allTtl = ent018.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0019":
			DelQty.delete(0, END)
			allTtl = ent019.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0020":
			DelQty.delete(0, END)
			allTtl = ent020.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0021":
			DelQty.delete(0, END)
			allTtl = ent021.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0022":
			DelQty.delete(0, END)
			allTtl = ent022.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0023":
			DelQty.delete(0, END)
			allTtl = ent023.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0024":
			DelQty.delete(0, END)
			allTtl = ent024.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0025":
			DelQty.delete(0, END)
			allTtl = ent025.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0026":
			DelQty.delete(0, END)
			allTtl = ent026.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0027":
			DelQty.delete(0, END)
			allTtl = ent027.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0028":
			DelQty.delete(0, END)
			allTtl = ent028.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0029":
			DelQty.delete(0, END)
			allTtl = ent029.get()
			DelQty.insert(0, allTtl)
		elif tempa == "0030":
			DelQty.delete(0, END)
			allTtl = ent030.get()
			DelQty.insert(0, allTtl)
		else:
			messagebox.showinfo("Notice", "Error Occured")

def remstc(tempa):
	if DelQty.get() == "" and DelEnt.get() == "":
		messagebox.showinfo("Notice", "Please specify the ID and quantity")
	elif DelQty.get() == "" and DelEnt.get() != "":
		messagebox.showinfo("Notice", "Please specify the quantity (or click all)")
	elif DelQty.get() != "" and DelEnt.get() == "":
		messagebox.showinfo("Notice", "Please specify the ID")
	else:
		if tempa == "0001":
			newT = int(ent001.get()) - int(DelQty.get())
			ent001.delete(0, END)
			ent001.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0002":
			newT = int(ent002.get()) - int(DelQty.get())
			ent002.delete(0, END)
			ent002.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0003":
			newT = int(ent003.get()) - int(DelQty.get())
			ent003.delete(0, END)
			ent003.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0004":
			newT = int(ent004.get()) - int(DelQty.get())
			ent004.delete(0, END)
			ent004.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0005":
			newT = int(ent005.get()) - int(DelQty.get())
			ent005.delete(0, END)
			ent005.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0006":
			newT = int(ent006.get()) - int(DelQty.get())
			ent006.delete(0, END)
			ent006.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0007":
			newT = int(ent007.get()) - int(DelQty.get())
			ent007.delete(0, END)
			ent007.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0008":
			newT = int(ent008.get()) - int(DelQty.get())
			ent008.delete(0, END)
			ent008.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0009":
			newT = int(ent009.get()) - int(DelQty.get())
			ent009.delete(0, END)
			ent009.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0010":
			newT = int(ent010.get()) - int(DelQty.get())
			ent010.delete(0, END)
			ent010.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0011":
			newT = int(ent011.get()) - int(DelQty.get())
			ent011.delete(0, END)
			ent011.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0012":
			newT = int(ent012.get()) - int(DelQty.get())
			ent012.delete(0, END)
			ent012.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0013":
			newT = int(ent013.get()) - int(DelQty.get())
			ent013.delete(0, END)
			ent013.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0014":
			newT = int(ent014.get()) - int(DelQty.get())
			ent014.delete(0, END)
			ent014.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0015":
			newT = int(ent015.get()) - int(DelQty.get())
			ent015.delete(0, END)
			ent015.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0016":
			newT = int(ent016.get()) - int(DelQty.get())
			ent016.delete(0, END)
			ent016.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0017":
			newT = int(ent017.get()) - int(DelQty.get())
			ent017.delete(0, END)
			ent017.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0018":
			newT = int(ent018.get()) - int(DelQty.get())
			ent018.delete(0, END)
			ent018.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0019":
			newT = int(ent019.get()) - int(DelQty.get())
			ent019.delete(0, END)
			ent019.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0020":
			newT = int(ent020.get()) - int(DelQty.get())
			ent020.delete(0, END)
			ent020.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0021":
			newT = int(ent021.get()) - int(DelQty.get())
			ent021.delete(0, END)
			ent021.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0022":
			newT = int(ent022.get()) - int(DelQty.get())
			ent022.delete(0, END)
			ent022.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0023":
			newT = int(ent023.get()) - int(DelQty.get())
			ent023.delete(0, END)
			ent023.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0024":
			newT = int(ent024.get()) - int(DelQty.get())
			ent024.delete(0, END)
			ent024.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0025":
			newT = int(ent025.get()) - int(DelQty.get())
			ent025.delete(0, END)
			ent025.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0026":
			newT = int(ent026.get()) - int(DelQty.get())
			ent026.delete(0, END)
			ent026.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0027":
			newT = int(ent027.get()) - int(DelQty.get())
			ent027.delete(0, END)
			ent027.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0028":
			newT = int(ent028.get()) - int(DelQty.get())
			ent028.delete(0, END)
			ent028.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0029":
			newT = int(ent029.get()) - int(DelQty.get())
			ent029.delete(0, END)
			ent029.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		elif tempa == "0030":
			newT = int(ent030.get()) - int(DelQty.get())
			ent030.delete(0, END)
			ent030.insert(0, newT)
			messagebox.showinfo("Notice", "Operation Successful")
			DelQty.delete(0, END)
			DelEnt.delete(0, END)
		else:
			messagebox.showinfo("Notice", "ID not Found")

# ___________________________________________________________
def svChng():
	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	cursr.execute("""UPDATE tblStocks SET
		attr01 = :attr01,
		attr02 = :attr02,
		attr03 = :attr03,
		attr04 = :attr04,
		attr05 = :attr05,
		attr06 = :attr06,
		attr07 = :attr07,
		attr08 = :attr08,
		attr09 = :attr09,
		attr10 = :attr10,
		attr11 = :attr11,
		attr12 = :attr12,
		attr13 = :attr13,
		attr14 = :attr14,
		attr15 = :attr15,
		attr16 = :attr16,
		attr17 = :attr17,
		attr18 = :attr18,
		attr19 = :attr19,
		attr20 = :attr20,
		attr21 = :attr21,
		attr22 = :attr22,
		attr23 = :attr23,
		attr24 = :attr24,
		attr25 = :attr25,
		attr26 = :attr26,
		attr27 = :attr27,
		attr28 = :attr28,
		attr29 = :attr29,
		attr30 = :attr30
		
		WHERE oid=1""",
		{
		'attr01' : ent001.get(),
		'attr02' : ent002.get(),
		'attr03' : ent003.get(),
		'attr04' : ent004.get(),
		'attr05' : ent005.get(),
		'attr06' : ent006.get(),
		'attr07' : ent007.get(),
		'attr08' : ent008.get(),
		'attr09' : ent009.get(),
		'attr10' : ent010.get(),
		'attr11' : ent011.get(),
		'attr12' : ent012.get(),
		'attr13' : ent013.get(),
		'attr14' : ent014.get(),
		'attr15' : ent015.get(),
		'attr16' : ent016.get(),
		'attr17' : ent017.get(),
		'attr18' : ent018.get(),
		'attr19' : ent019.get(),
		'attr20' : ent020.get(),
		'attr21' : ent021.get(),
		'attr22' : ent022.get(),
		'attr23' : ent023.get(),
		'attr24' : ent024.get(),
		'attr25' : ent025.get(),
		'attr26' : ent026.get(),
		'attr27' : ent027.get(),
		'attr28' : ent028.get(),
		'attr29' : ent029.get(),
		'attr30' : ent030.get()
		})

	cnnct.commit()
	cnnct.close()

	confirm = messagebox.askquestion("Notice", "Do you want to save the changes?")
	if confirm == "yes":
		Stocks()
		messagebox.showinfo("Notice", "Changes were successfully saved")
		hnseek(2)
	else:
		messagebox.showinfo("Notice", "Cancelled by the user")

# ___________________________________________________________
def vwtrns():	

	cnnct = sqlite3.connect('RevisedProj.db')
	cursr = cnnct.cursor()

	cursr.execute("SELECT *, oid FROM tblOrderList")
	crrnt = cursr.fetchall()

	con_03 = Tk()
	con_03.title('View Transaction/s')
	con_03.geometry('700x650')
	con_03.iconbitmap('Images/icon.ico')
	con_03.resizable(False, False)

	frm_aa = LabelFrame(con_03, width=650, height=600)
	frm_ab = LabelFrame(con_03, width=650, height=20)

	cvs_ms = Canvas(frm_aa, width=650, height=540, bg="white")
	scr_ms = ttk.Scrollbar(frm_aa, orient=VERTICAL, command=cvs_ms.yview)
	cvs_ms.configure(yscrollcommand=scr_ms.set, highlightthickness=0)
	pvt_01 = Frame(cvs_ms, bg="white")
	cvs_ms.create_window((0, 0), window=pvt_01, anchor="nw")

	prvt_lbl_0 = Label(pvt_01, text="Transac. No.", font="arial 15 bold", bg="white").grid(row=0, column=0)
	prvt_lbl_1 = Label(pvt_01, text="Total", font="arial 15 bold", bg="white", justify=LEFT).grid(row=0, column=1, sticky=W, padx=(20, 0))
	prvt_lbl_2 = Label(pvt_01, text="Order List", font="arial 15 bold", bg="white", justify=LEFT).grid(row=0, column=2, sticky=W, padx=(20, 0))

	count = 0
	totalSale = 0
	for record in crrnt:
		count += 1

		total = float(record[0])
		list_ = record[1]
		id_no = record[2]
		
		lid = 'lid'+str(count)
		lid = Label(pvt_01, text=id_no, justify=LEFT)
		lid.grid(row=count, column=0, sticky=E+N, pady=(5, 0))
		
		lbz = 'lbz'+str(count)
		lbz = Label(pvt_01, text="P"+str(total), justify=LEFT)
		lbz.grid(row=count, column=1, sticky=E+N, padx=(20, 0), pady=(5, 0))
		totalSale += float(total)

		lbl = 'lbl'+str(count)
		lbl = Label(pvt_01, text=list_, justify=LEFT)
		lbl.grid(row=count, column=2, sticky=W, padx=(20, 0), pady=(5, 0))

	cvsms1 = Canvas(frm_ab, width=647, height=60, bg="white")
	pvt_02 = Frame(cvsms1, bg="white")
	cvsms1.create_window((0, 0), window=pvt_02, anchor="nw")

	lbl99 = Label(pvt_02, text="Total Sales: ", bg="white", font="arial 15 bold").grid(row=0, column=0, padx=(425, 0), pady=20)
	lbl98 = Label(pvt_02, text="P"+str(totalSale), bg="white", font="arial 15 normal").grid(row=0, column=1, pady=20)

	cvs_ms.grid(row=0, column=0)
	scr_ms.place(x=632, y=0, height=540)
	cvs_ms.configure(yscrollcommand=scr_ms.set)
	cvs_ms.bind('<Configure>', lambda e: cvs_ms.configure(scrollregion=cvs_ms.bbox("all")))

	cvsms1.grid(row=0, column=0)
	
	frm_aa.place(x=25, y=15)
	frm_ab.place(x=25, y=570)

	cnnct.commit()
	cnnct.close()

# ___________________________________________________________
def addbtn(tempo, tempu):
	if tempo == 1:
		newT = int(tempu) + 1
		ent001.delete(0, END)
		ent001.insert(0, newT)
	elif tempo == 2:
		newT = int(tempu) + 1
		ent002.delete(0, END)
		ent002.insert(0, newT)
	elif tempo == 3:
		newT = int(tempu) + 1
		ent003.delete(0, END)
		ent003.insert(0, newT)	
	elif tempo == 4:
		newT = int(tempu) + 1
		ent004.delete(0, END)
		ent004.insert(0, newT)	
	elif tempo == 5:
		newT = int(tempu) + 1
		ent005.delete(0, END)
		ent005.insert(0, newT)	
	elif tempo == 6:
		newT = int(tempu) + 1
		ent006.delete(0, END)
		ent006.insert(0, newT)	
	elif tempo == 7:
		newT = int(tempu) + 1
		ent007.delete(0, END)
		ent007.insert(0, newT)	
	elif tempo == 8:
		newT = int(tempu) + 1
		ent008.delete(0, END)
		ent008.insert(0, newT)	
	elif tempo == 9:
		newT = int(tempu) + 1
		ent009.delete(0, END)
		ent009.insert(0, newT)	
	elif tempo == 10:
		newT = int(tempu) + 1
		ent010.delete(0, END)
		ent010.insert(0, newT)	
	elif tempo == 11:
		newT = int(tempu) + 1
		ent011.delete(0, END)
		ent011.insert(0, newT)	
	elif tempo == 12:
		newT = int(tempu) + 1
		ent012.delete(0, END)
		ent012.insert(0, newT)	
	elif tempo == 13:
		newT = int(tempu) + 1
		ent013.delete(0, END)
		ent013.insert(0, newT)	
	elif tempo == 14:
		newT = int(tempu) + 1
		ent014.delete(0, END)
		ent014.insert(0, newT)	
	elif tempo == 15:
		newT = int(tempu) + 1
		ent015.delete(0, END)
		ent015.insert(0, newT)	
	elif tempo == 16:
		newT = int(tempu) + 1
		ent016.delete(0, END)
		ent016.insert(0, newT)	
	elif tempo == 17:
		newT = int(tempu) + 1
		ent017.delete(0, END)
		ent017.insert(0, newT)	
	elif tempo == 18:
		newT = int(tempu) + 1
		ent018.delete(0, END)
		ent018.insert(0, newT)	
	elif tempo == 19:
		newT = int(tempu) + 1
		ent019.delete(0, END)
		ent019.insert(0, newT)	
	elif tempo == 20:
		newT = int(tempu) + 1
		ent020.delete(0, END)
		ent020.insert(0, newT)	
	elif tempo == 21:
		newT = int(tempu) + 1
		ent021.delete(0, END)
		ent021.insert(0, newT)	
	elif tempo == 22:
		newT = int(tempu) + 1
		ent022.delete(0, END)
		ent022.insert(0, newT)	
	elif tempo == 23:
		newT = int(tempu) + 1
		ent023.delete(0, END)
		ent023.insert(0, newT)	
	elif tempo == 24:
		newT = int(tempu) + 1
		ent024.delete(0, END)
		ent024.insert(0, newT)	
	elif tempo == 25:
		newT = int(tempu) + 1
		ent025.delete(0, END)
		ent025.insert(0, newT)	
	elif tempo == 26:
		newT = int(tempu) + 1
		ent026.delete(0, END)
		ent026.insert(0, newT)	
	elif tempo == 27:
		newT = int(tempu) + 1
		ent027.delete(0, END)
		ent027.insert(0, newT)	
	elif tempo == 28:
		newT = int(tempu) + 1
		ent028.delete(0, END)
		ent028.insert(0, newT)	
	elif tempo == 29:
		newT = int(tempu) + 1
		ent029.delete(0, END)
		ent029.insert(0, newT)	
	else:
		newT = int(tempu) + 1
		ent030.delete(0, END)
		ent030.insert(0, newT)

# ___________________________________________________________
def subbtn(tempo, tempu):
	if tempo == 1:
		newT = int(tempu) - 1
		ent001.delete(0, END)
		ent001.insert(0, newT)
	elif tempo == 2:
		newT = int(tempu) - 1
		ent002.delete(0, END)
		ent002.insert(0, newT)
	elif tempo == 3:
		newT = int(tempu) - 1
		ent003.delete(0, END)
		ent003.insert(0, newT)	
	elif tempo == 4:
		newT = int(tempu) - 1
		ent004.delete(0, END)
		ent004.insert(0, newT)	
	elif tempo == 5:
		newT = int(tempu) - 1
		ent005.delete(0, END)
		ent005.insert(0, newT)	
	elif tempo == 6:
		newT = int(tempu) - 1
		ent006.delete(0, END)
		ent006.insert(0, newT)	
	elif tempo == 7:
		newT = int(tempu) - 1
		ent007.delete(0, END)
		ent007.insert(0, newT)	
	elif tempo == 8:
		newT = int(tempu) - 1
		ent008.delete(0, END)
		ent008.insert(0, newT)	
	elif tempo == 9:
		newT = int(tempu) - 1
		ent009.delete(0, END)
		ent009.insert(0, newT)	
	elif tempo == 10:
		newT = int(tempu) - 1
		ent010.delete(0, END)
		ent010.insert(0, newT)	
	elif tempo == 11:
		newT = int(tempu) - 1
		ent011.delete(0, END)
		ent011.insert(0, newT)	
	elif tempo == 12:
		newT = int(tempu) - 1
		ent012.delete(0, END)
		ent012.insert(0, newT)	
	elif tempo == 13:
		newT = int(tempu) - 1
		ent013.delete(0, END)
		ent013.insert(0, newT)	
	elif tempo == 14:
		newT = int(tempu) - 1
		ent014.delete(0, END)
		ent014.insert(0, newT)	
	elif tempo == 15:
		newT = int(tempu) - 1
		ent015.delete(0, END)
		ent015.insert(0, newT)	
	elif tempo == 16:
		newT = int(tempu) - 1
		ent016.delete(0, END)
		ent016.insert(0, newT)	
	elif tempo == 17:
		newT = int(tempu) - 1
		ent017.delete(0, END)
		ent017.insert(0, newT)	
	elif tempo == 18:
		newT = int(tempu) - 1
		ent018.delete(0, END)
		ent018.insert(0, newT)	
	elif tempo == 19:
		newT = int(tempu) - 1
		ent019.delete(0, END)
		ent019.insert(0, newT)	
	elif tempo == 20:
		newT = int(tempu) - 1
		ent020.delete(0, END)
		ent020.insert(0, newT)	
	elif tempo == 21:
		newT = int(tempu) - 1
		ent021.delete(0, END)
		ent021.insert(0, newT)	
	elif tempo == 22:
		newT = int(tempu) - 1
		ent022.delete(0, END)
		ent022.insert(0, newT)	
	elif tempo == 23:
		newT = int(tempu) - 1
		ent023.delete(0, END)
		ent023.insert(0, newT)	
	elif tempo == 24:
		newT = int(tempu) - 1
		ent024.delete(0, END)
		ent024.insert(0, newT)	
	elif tempo == 25:
		newT = int(tempu) - 1
		ent025.delete(0, END)
		ent025.insert(0, newT)	
	elif tempo == 26:
		newT = int(tempu) - 1
		ent026.delete(0, END)
		ent026.insert(0, newT)	
	elif tempo == 27:
		newT = int(tempu) - 1
		ent027.delete(0, END)
		ent027.insert(0, newT)	
	elif tempo == 28:
		newT = int(tempu) - 1
		ent028.delete(0, END)
		ent028.insert(0, newT)	
	elif tempo == 29:
		newT = int(tempu) - 1
		ent029.delete(0, END)
		ent029.insert(0, newT)	
	else:
		newT = int(tempu) - 1
		ent030.delete(0, END)
		ent030.insert(0, newT)

def hnseek(tmprry):
	if tmprry == 1:
		con_01.destroy()
	else:
		con_02.destroy()

	container.deiconify()
	EntStc.delete(0, END)
	EntTtl.delete(0, END)
	EntQty.delete(0, END)
	txtlft.delete(1.0, END)

# ___________________________________________________________
img_00 = PhotoImage(file="Images/a_tab/yammodel.png")
img_01 = PhotoImage(file="Images/a_tab/CJSModel.png")
img_02 = PhotoImage(file="Images/a_tab/CJModel.png")
img_03 = PhotoImage(file="Images/a_tab/CJBSModel.png")
img_04 = PhotoImage(file="Images/a_tab/JSModel.png")
img_05 = PhotoImage(file="Images/a_tab/2CJModel.png")
img_06 = PhotoImage(file="Images/a_tab/CYBModel.png")

img_07 = PhotoImage(file="Images/b_tab/BPModel.png")
img_08 = PhotoImage(file="Images/b_tab/CAJSModel.png")
img_09 = PhotoImage(file="Images/b_tab/CFModel.png")
img_10 = PhotoImage(file="Images/b_tab/CHSModel.png")
img_11 = PhotoImage(file="Images/b_tab/HBRSModel.png")
img_12 = PhotoImage(file="Images/b_tab/TPModel.png")

img_13 = PhotoImage(file="Images/c_tab/RTCModel.png")

img_14 = PhotoImage(file="Images/d_tab/4CFBLFModel.png")
img_15 = PhotoImage(file="Images/d_tab/4CJFBSModel.png")
img_16 = PhotoImage(file="Images/d_tab/6CSModel.png")
img_17 = PhotoImage(file="Images/d_tab/8CSModel.png")
img_18 = PhotoImage(file="Images/d_tab/CFBModel.png")

img_19 = PhotoImage(file="Images/e_tab/1BCJModel.png")
img_20 = PhotoImage(file="Images/e_tab/BTModel.png")
img_21 = PhotoImage(file="Images/e_tab/CBModel.png")
img_22 = PhotoImage(file="Images/e_tab/LModel.png")

img_23 = PhotoImage(file="Images/f_tab/4CFBLFModel.png")
img_24 = PhotoImage(file="Images/f_tab/4CFBSModel.png")
img_25 = PhotoImage(file="Images/f_tab/6CJSModel.png")
img_26 = PhotoImage(file="Images/f_tab/8CJSModel.png")

img_27 = PhotoImage(file="Images/g_tab/2SCCDModel.png")
img_28 = PhotoImage(file="Images/g_tab/2SCCSModel.png")
img_29 = PhotoImage(file="Images/g_tab/4SCCSModel.png")
img_30 = PhotoImage(file="Images/g_tab/6SCCSModel.png")

img_31 = PhotoImage(file="Images/h_tab/CJSMModel.png")
img_32 = PhotoImage(file="Images/h_tab/CKODModel.png")
img_33 = PhotoImage(file="Images/h_tab/SCJModel.png")
img_34 = PhotoImage(file="Images/h_tab/SCModel.png")

# ___________________________________________________________
nbk_00 = ttk.Notebook(container, width=800, height=570)
frm_01 = Frame(nbk_00, bg='white')
frm_02 = Frame(nbk_00, bg='white')
frm_03 = Frame(nbk_00, bg='white')
frm_04 = Frame(nbk_00, bg='white')
frm_05 = Frame(nbk_00, bg='white')
frm_06 = Frame(nbk_00, bg='white')
frm_07 = Frame(nbk_00, bg='white')
frm_08 = Frame(nbk_00, bg='white')

nbk_00.add(frm_01, text="Best-Sellers       ")
nbk_00.add(frm_02, text="New-Products       ")
nbk_00.add(frm_03, text="Ready-to-Cook      ")
nbk_00.add(frm_04, text="Family-Meals       ")
nbk_00.add(frm_05, text="Breakfast          ")
nbk_00.add(frm_06, text="Chicken-Joy        ")
nbk_00.add(frm_07, text="Sweet-Chili Chicken")
nbk_00.add(frm_08, text="Burgers            ")

cvs_00 = Canvas(frm_01, width=800, height=570, bg="white")
scr_00 = ttk.Scrollbar(frm_01, orient=VERTICAL, command=cvs_00.yview)
cvs_00.configure(yscrollcommand=scr_00.set)
sub_f1 = Frame(cvs_00, bg="white")
cvs_00.create_window((0, 0), window=sub_f1, anchor="nw")

cvs_01 = Canvas(frm_02, width=800, height=570, bg="white")
scr_01 = ttk.Scrollbar(frm_02, orient=VERTICAL, command=cvs_01.yview)
cvs_01.configure(yscrollcommand=scr_01.set)
sub_f2 = Frame(cvs_01, bg="white")
cvs_01.create_window((0, 0), window=sub_f2, anchor="nw")

cvs_03 = Canvas(frm_04, width=800, height=570, bg="white")
scr_03 = ttk.Scrollbar(frm_04, orient=VERTICAL, command=cvs_03.yview)
cvs_03.configure(yscrollcommand=scr_03.set)
sub_f4 = Frame(cvs_03, bg="white")
cvs_03.create_window((0, 0), window=sub_f4, anchor="nw")

cvs_04 = Canvas(frm_05, width=800, height=570, bg="white")
scr_04 = ttk.Scrollbar(frm_05, orient=VERTICAL, command=cvs_04.yview)
cvs_04.configure(yscrollcommand=scr_04.set)
sub_f5 = Frame(cvs_04, bg="white")
cvs_04.create_window((0, 0), window=sub_f5, anchor="nw")

cvs_05 = Canvas(frm_06, width=800, height=570, bg="white")
scr_05 = ttk.Scrollbar(frm_06, orient=VERTICAL, command=cvs_05.yview)
cvs_05.configure(yscrollcommand=scr_05.set)
sub_f6 = Frame(cvs_05, bg="white")
cvs_05.create_window((0, 0), window=sub_f6, anchor="nw")

cvs_06 = Canvas(frm_07, width=800, height=570, bg="white")
scr_06 = ttk.Scrollbar(frm_07, orient=VERTICAL, command=cvs_06.yview)
cvs_06.configure(yscrollcommand=scr_06.set)
sub_f7 = Frame(cvs_06, bg="white")
cvs_06.create_window((0, 0), window=sub_f7, anchor="nw")

cvs_07 = Canvas(frm_08, width=800, height=570, bg="white")
scr_07 = ttk.Scrollbar(frm_08, orient=VERTICAL, command=cvs_07.yview)
cvs_07.configure(yscrollcommand=scr_07.set)
sub_f8 = Frame(cvs_07, bg="white")
cvs_07.create_window((0, 0), window=sub_f8, anchor="nw")

nbk_00.place(x=330, y=20)
cvs_00.grid(row=0, column=0)
scr_00.place(x=783, y=0, height=570)
cvs_00.configure(yscrollcommand=scr_00.set)
cvs_00.bind('<Configure>', lambda e: cvs_00.configure(scrollregion=cvs_00.bbox("all")))

cvs_01.grid(row=0, column=0)
scr_01.place(x=783, y=0, height=570)
cvs_01.configure(yscrollcommand=scr_01.set)
cvs_01.bind('<Configure>', lambda e: cvs_01.configure(scrollregion=cvs_01.bbox("all")))

cvs_03.grid(row=0, column=0)
scr_03.place(x=783, y=0, height=570)
cvs_03.configure(yscrollcommand=scr_03.set)
cvs_03.bind('<Configure>', lambda e: cvs_03.configure(scrollregion=cvs_03.bbox("all")))

cvs_04.grid(row=0, column=0)
scr_04.place(x=783, y=0, height=570)
cvs_04.configure(yscrollcommand=scr_04.set)
cvs_04.bind('<Configure>', lambda e: cvs_04.configure(scrollregion=cvs_04.bbox("all")))

cvs_05.grid(row=0, column=0)
scr_05.place(x=783, y=0, height=570)
cvs_05.configure(yscrollcommand=scr_05.set)
cvs_05.bind('<Configure>', lambda e: cvs_05.configure(scrollregion=cvs_05.bbox("all")))

cvs_06.grid(row=0, column=0)
scr_06.place(x=783, y=0, height=570)
cvs_06.configure(yscrollcommand=scr_06.set)
cvs_06.bind('<Configure>', lambda e: cvs_06.configure(scrollregion=cvs_06.bbox("all")))

cvs_07.grid(row=0, column=0)
scr_07.place(x=783, y=0, height=570)
cvs_07.configure(yscrollcommand=scr_07.set)
cvs_07.bind('<Configure>', lambda e: cvs_07.configure(scrollregion=cvs_07.bbox("all")))

# ___________________________________________________________
sfr_01 = Frame(container)
lblStc = Label(sfr_01, text="Stocks")
lblQty = Label(sfr_01, text="Quantity")
lblTtl = Label(sfr_01, text="Total")
EntStc = Entry(sfr_01, justify=RIGHT)
EntQty = Entry(sfr_01, width=37, justify=RIGHT)
EntTtl = Entry(sfr_01, justify=RIGHT)

sfr_01.place(x=30, y=320)
lblStc.grid(row=0, column=0, sticky=W, pady=(0, 20))
lblQty.grid(row=1, column=0)
lblTtl.grid(row=2, column=0, sticky=W)
EntStc.grid(row=0, column=1, sticky=W+E, pady=(0, 20))
EntQty.grid(row=1, column=1)
EntTtl.grid(row=2, column=1, sticky=W+E)

# ___________________________________________________________
sfr_02 = Frame(container)
btn_00 = Button(container, relief=RIDGE, text="View Transactions", command=vwtrns)
btn_01 = Button(container, relief=RIDGE, padx=5, text="View Stocks", command=vwStck)
btn_02 = Button(container, relief=RIDGE, padx=3, text="Manage Stocks", command=mgStck)

btn_03 = Button(sfr_02, relief=GROOVE, text="1", padx=20, pady=20, command = lambda: btnQty(1))
btn_04 = Button(sfr_02, relief=GROOVE, text="2", padx=20, pady=20, command = lambda: btnQty(2))
btn_05 = Button(sfr_02, relief=GROOVE, text="3", padx=20, pady=20, command = lambda: btnQty(3))
btn_06 = Button(sfr_02, relief=GROOVE, text="4", padx=20, pady=20, command = lambda: btnQty(4))
btn_07 = Button(sfr_02, relief=GROOVE, text="5", padx=20, pady=20, command = lambda: btnQty(5))
btn_08 = Button(sfr_02, relief=GROOVE, text="6", padx=20, pady=20, command = lambda: btnQty(6))
btn_09 = Button(sfr_02, relief=GROOVE, text="7", padx=20, pady=20, command = lambda: btnQty(7))
btn_10 = Button(sfr_02, relief=GROOVE, text="8", padx=20, pady=20, command = lambda: btnQty(8))
btn_11 = Button(sfr_02, relief=GROOVE, text="9", padx=20, pady=20, command = lambda: btnQty(9))

btn_13 = Button(sfr_02, relief=GROOVE, text="Cancel", bg="#B22222", fg="white", command=backup)
btn_14 = Button(sfr_02, relief=GROOVE, text="Clear", pady=20, command=fClear)
btn_15 = Button(sfr_02, relief=GROOVE, text="Place Order", pady=20, bg="#32CD32", fg="white", command=plcOrd)

btn_16 = Button(sub_f1, image=img_00, bd=1, command=lambda: btnOrd(1))
btn_17 = Button(sub_f1, image=img_01, bd=1, command=lambda: btnOrd(2))
btn_18 = Button(sub_f1, image=img_02, bd=1, command=lambda: btnOrd(3))
btn_19 = Button(sub_f1, image=img_04, bd=1, command=lambda: btnOrd(4))
btn_20 = Button(sub_f1, image=img_03, bd=1, command=lambda: btnOrd(5))
btn_21 = Button(sub_f1, image=img_05, bd=1, command=lambda: btnOrd(6))
btn_22 = Button(sub_f1, image=img_06, bd=1, command=lambda: btnOrd(7))
btn_23 = Button(sub_f2, image=img_07, bd=1, command=lambda: btnOrd(8))
btn_24 = Button(sub_f2, image=img_08, bd=1, command=lambda: btnOrd(9))
btn_25 = Button(sub_f2, image=img_09, bd=1, command=lambda: btnOrd(10))
btn_26 = Button(sub_f2, image=img_10, bd=1, command=lambda: btnOrd(11))
btn_27 = Button(sub_f2, image=img_11, bd=1, command=lambda: btnOrd(12))
btn_28 = Button(sub_f2, image=img_12, bd=1, command=lambda: btnOrd(13))

btn_29 = Button(frm_03, image=img_13, bd=1, command=lambda: btnOrd(14))

btn_30 = Button(sub_f4, image=img_14, bd=1, command=lambda: btnOrd(15))
btn_31 = Button(sub_f4, image=img_15, bd=1, command=lambda: btnOrd(16))
btn_32 = Button(sub_f4, image=img_16, bd=1, command=lambda: btnOrd(17))
btn_33 = Button(sub_f4, image=img_17, bd=1, command=lambda: btnOrd(18))
btn_34 = Button(sub_f4, image=img_18, bd=1, command=lambda: btnOrd(19))

btn_35 = Button(sub_f5, image=img_19, bd=1, command=lambda: btnOrd(20))
btn_36 = Button(sub_f5, image=img_20, bd=1, command=lambda: btnOrd(21))
btn_37 = Button(sub_f5, image=img_21, bd=1, command=lambda: btnOrd(22))
btn_38 = Button(sub_f5, image=img_22, bd=1, command=lambda: btnOrd(23))

btn_39 = Button(sub_f6, image=img_23, bd=1, command=lambda: btnOrd(24))
btn_40 = Button(sub_f6, image=img_24, bd=1, command=lambda: btnOrd(25))
btn_41 = Button(sub_f6, image=img_25, bd=1, command=lambda: btnOrd(26))
btn_42 = Button(sub_f6, image=img_26, bd=1, command=lambda: btnOrd(27))

btn_43 = Button(sub_f7, image=img_27, bd=1, command=lambda: btnOrd(28))
btn_44 = Button(sub_f7, image=img_28, bd=1, command=lambda: btnOrd(29))
btn_45 = Button(sub_f7, image=img_29, bd=1, command=lambda: btnOrd(30))
btn_46 = Button(sub_f7, image=img_30, bd=1, command=lambda: btnOrd(31))

btn_47 = Button(sub_f8, image=img_31, bd=1, command=lambda: btnOrd(32))
btn_48 = Button(sub_f8, image=img_32, bd=1, command=lambda: btnOrd(33))
btn_49 = Button(sub_f8, image=img_33, bd=1, command=lambda: btnOrd(34))
btn_50 = Button(sub_f8, image=img_34, bd=1, command=lambda: btnOrd(35))

sfr_02.place(x=30, y=415)
btn_00.place(x=20, y=20)
btn_01.place(x=130, y=20)
btn_02.place(x=217, y=20)

btn_03.grid(row=0, column=0, padx=(0, 2), pady=(0, 2))
btn_04.grid(row=0, column=1, padx=(0, 2), pady=(0, 2))
btn_05.grid(row=0, column=2, padx=(0, 2), pady=(0, 2))
btn_06.grid(row=0, column=3, padx=(0, 2), pady=(0, 2))
btn_07.grid(row=0, column=4, padx=(0, 2), pady=(0, 2))
btn_08.grid(row=1, column=0, padx=(0, 2), pady=(0, 2))
btn_09.grid(row=1, column=1, padx=(0, 2), pady=(0, 2))
btn_10.grid(row=1, column=2, padx=(0, 2), pady=(0, 2))
btn_11.grid(row=1, column=3, padx=(0, 2), pady=(0, 2))
btn_13.grid(row=2, column=0, columnspan=2, sticky=E+W+N+S, padx=(0, 2), pady=(0, 2))
btn_14.grid(row=1, column=4, rowspan=2, sticky=E+W+N+S, padx=(0, 2), pady=(0, 2))
btn_15.grid(row=2, column=2, columnspan=2, sticky=E+W, padx=(0, 2), pady=(0, 2))

btn_16.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_17.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_18.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_19.grid(row=1, column=0, padx=(4, 2), pady=2)
btn_20.grid(row=1, column=1, padx=2, pady=2)
btn_21.grid(row=1, column=2, padx=2,  pady=2)
btn_22.grid(row=2, column=0, padx=(4, 2), pady=(2, 4))

btn_23.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_24.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_25.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_26.grid(row=1, column=0, padx=(4, 2), pady=2)
btn_27.grid(row=1, column=1, padx=2, pady=2)
btn_28.grid(row=1, column=2, padx=2,  pady=2)

btn_29.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))

btn_30.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_31.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_32.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_33.grid(row=1, column=0, padx=(4, 2), pady=2)
btn_34.grid(row=1, column=1, padx=2, pady=2)

btn_35.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_36.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_37.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_38.grid(row=1, column=0, padx=(4, 2), pady=2)

btn_39.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_40.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_41.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_42.grid(row=1, column=0, padx=(4, 2), pady=2)

btn_43.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_44.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_45.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_46.grid(row=1, column=0, padx=(4, 2), pady=2)

btn_47.grid(row=0, column=0, padx=(4, 2), pady=(4, 2))
btn_48.grid(row=0, column=1, padx=4, pady=(4, 2))
btn_49.grid(row=0, column=2, padx=(2, 4), pady=(4, 2))
btn_50.grid(row=1, column=0, padx=(4, 2), pady=2)

frmlft = Frame(container, width=290, height=250, bg="white")
cvslft = Canvas(frmlft, bg="white", bd=0)
txtlft = Text(cvslft, width=36, height=100, font="arial 9 normal")

frmlft.place(x=20, y=55)
cvslft.place(x=0, y=0)
txtlft.place(x=0, y=0)

container.mainloop()
