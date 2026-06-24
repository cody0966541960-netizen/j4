import customtkinter as ctk
from database import DatabaseEngine
from view_home import HomeView
from view_stats import StatsView

# 設定視窗整體主題
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        # 視窗標題與大小設定
        self.title("🧠 多巴胺自律管理系統 v3.1")
        self.geometry("600x750")

        # 初始化資料庫引擎
        self.db = DatabaseEngine()

        # --- 側邊/上方導覽列按鈕 ---
        self.nav_frame = ctk.CTkFrame(self, height=50)
        self.nav_frame.pack(fill="x", padx=20, pady=10)

        self.btn_home = ctk.CTkButton(self.nav_frame, text="🏠 主頁紀錄", command=self.show_home)
        self.btn_home.pack(side="left", padx=10, pady=5)

        self.btn_stats = ctk.CTkButton(self.nav_frame, text="📊 統計分析", command=self.show_stats, fg_color="purple", hover_color="darkpurple")
        self.btn_stats.pack(side="left", padx=10, pady=5)

        # --- 頁面容器 (Container) ---
        self.container = ctk.CTkFrame(self, width=550, height=650, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=20, pady=10)

        # 初始化各個頁面並傳入同一個資料庫引擎執行聯動
        self.frames = {}
        self.frames["Home"] = HomeView(self.container, self.db)
        self.frames["Stats"] = StatsView(self.container, self.db)

        # 預設顯示主頁
        self.show_home()

    def show_page(self, page_name):
        """將指定的頁面推到最前方顯示"""
        # 先隱藏所有頁面
        for frame in self.frames.values():
            frame.pack_forget()
        # 顯示目標頁面
        self.frames[page_name].pack(fill="both", expand=True)

    def show_home(self):
        self.frames["Home"].refresh_display() # 切換回去時重新整理數據
        self.show_page("Home")

    def show_stats(self):
        self.show_page("Stats")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
