from fpdf import FPDF

class MY_PDF(FPDF):
    def header(self):
        # Arial bold 15
        #self.set_font('Arial', 'B', 15)
        # Move to the right
        #self.cell(80)
        # Title
        #self.cell(30, 10, title, 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # env
    def myEnv(self):
        self.add_font('sysfont', '', 'NEXONLv1GothicRegular.ttf')
        self.set_font("sysfont", size=10)
        line_height = self.font_size * 2.5
        pass

    def myHead(self, nameTitle):
        # head
        self.set_font(style='U')
        self.cell(w=0, h=10, txt=nameTitle, border=0, align='C')
        self.set_font(style='')
        line_height = self.font_size * 2.5
        self.ln(line_height * 2)

    def myBody_1row_2colume(self, name1Colume, name2Colume, pair_col1_col2):
        # contents
        line_height = self.font_size * 2.5
        col_width = self.epw / 2  # distribute content evenly
        for datum in pair_col1_col2:
            self.multi_cell(col_width, line_height, datum, border=0, new_x="RIGHT", new_y="TOP",
                           max_line_height=self.font_size)
        self.ln(line_height)

    def myBody_2columes(self, name1Colume, name2Colume, dataframe):
        for index in dataframe.index:
            eng = dataframe[name1Colume][index]
            kor = dataframe[name2Colume][index]
            data_row = (eng, kor)
            self.myBody_1row_2colume(name1Colume, name2Colume, data_row)

    def mySaveToFile(self, nameTitle):
        self.output(f'{nameTitle}.pdf')