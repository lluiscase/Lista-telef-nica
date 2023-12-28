import wx
import pywhatkit

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,size=(800, 520), )
        #Centraliza a interface
        self.Centre()
        #Coloca icone no frame
        self.SetIcon(wx.Icon("icon.png"))
        #Panel principal
        self.panel = wx.Panel(self)
        #Cria o gradiente pro Panel principal
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)

    #Cria a lista onde guarda os contatos
        self.listbox = wx.ListBox(self.panel, size = ((550,320)))
        self.listbox.SetBackgroundColour((43, 36, 52, 1))
        self.listbox.SetOwnForegroundColour(wx.WHITE)
        self.listbox.SetPosition(wx.Point(80, 100))

    #Cria o titulo da lista
        st = wx.StaticText(self.panel, label ="Lista de contato")
        st.SetPosition(wx.Point(100,88))
        st.SetBackgroundColour((43, 36, 52, 1))
        st.SetOwnForegroundColour(wx.WHITE)

    #Cria todo painel de botões no topo do Panel principal
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btnPanel = wx.Panel(self.panel,wx.EXPAND)
        btnPanel.SetBackgroundColour((43, 36, 52, 1))
        hbox.Add(btnPanel, 0.6,  wx.LEFT, 0)
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        btnPanel.SetSizer(vbox)
        self.panel.SetSizer(hbox)

    #Abre um input antes da interface para definir o nome
        direction = wx.GetTextFromUser('Digite o seu nome: ')
        name = wx.StaticText(self.panel,label = direction)
        name.SetOwnForegroundColour(wx.WHITE)
        name.SetBackgroundColour((43, 36, 52, 1))
        name.SetPosition(wx.Point(50,10))

    #Cria um botão para adicionar contatos na lista
        newBtn = wx.Bitmap("Plus.png", wx.BITMAP_TYPE_ANY)
        newBtn = wx.BitmapButton(btnPanel, id = wx.ID_ANY, bitmap = newBtn,
    size =(35,35))
        newBtn.SetBackgroundColour((43, 36, 52, 1))

    #Cria um botão para editar contatos na lista
        editBtn = wx.Bitmap("Vector.png", wx.BITMAP_TYPE_ANY)
        editBtn =wx.BitmapButton(btnPanel, id = wx.ID_ANY, bitmap = editBtn,
    size =(35,35))
        editBtn.SetBackgroundColour((43, 36, 52, 1))

        #Cria um botão para deletar contatos na lista
        delBtn = wx.Bitmap("trash.png", wx.BITMAP_TYPE_ANY)
        delBtn = wx.BitmapButton(btnPanel, id = wx.ID_ANY, bitmap = delBtn,
    size =(35,35))
        delBtn.SetBackgroundColour((43, 36, 52, 1))

        #Cria um botão para mensagem automatica no Whatsapp
        zapBtn = wx.Bitmap("zap.png", wx.BITMAP_TYPE_ANY)
        zapBtn = wx.BitmapButton(self.panel, id = wx.ID_ANY, bitmap = zapBtn,
    size =(35,35))
        zapBtn.SetBackgroundColour((43, 36, 52, 1))
        zapBtn.SetPosition(wx.Point(748,445))
        
        #Adiciona os botões no painel do topo
        vbox.Add((680, 10))
        vbox.Add(newBtn)
        vbox.Add(editBtn)
        vbox.Add(delBtn)

        #Define as funções/eventos de cada botão pegando seus ID
        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=editBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnWhatsapp, id=zapBtn.GetId())
  
  #Função que cria o gradiente
    def on_paint(self, event):
        dc = wx.PaintDC(self.panel)
        x = 0
        y = 0
        w, h = self.GetSize()
        dc.GradientFillLinear((x, y, w, h), wx.Colour(66, 39, 90),
                            wx.Colour(89, 56, 99))

  #Função que cria a ação do botão de adicionar algo na lista
    def NewItem(self, event):
        #Inputs para cada informação do contato
        text = wx.GetTextFromUser('Digite o nome do contato')
        numero = wx.GetTextFromUser('Digite o número')
        email = wx.GetTextFromUser('Digite o email')
        result = [f'Nome: {text}', f'Numero: +5511{numero}', f'Email: {email}']
        
        #Adiciona na lista
        if result != '':
            self.listbox.Append(result)
            self.listbox.Append('-------------*-------------')

  #Função que deleta o item selecionado na lista
    def OnDelete(self, event):
        #Pega o item selecionado
        sel = self.listbox.GetSelection()
        #Deleta o item selecionado
        self.listbox.Delete(sel)

    #Função que renomeia o item selecionado na lista
    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        selection = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Edite o item selecionado', selection)
        if renamed == '':
            wx.MessageBox('não deixe espaços em branco', 'Info')
        else:
            self.listbox.Delete(sel)
            self.listbox.Append(renamed)

    #Função que manda uma mensagem automatica no whatsapp
    def OnWhatsapp(self,event):
        sel = self.listbox.GetSelection()
        number = self.listbox.GetString(sel)
        message = wx.GetTextFromUser('Digite a mensagem que quer enviar')
        hour = wx.GetTextFromUser('Defina a hora de envio')
        min = wx.GetTextFromUser('Defina os minutos de envio')
        pywhatkit.sendwhatmsg("{}".format(number[8:22]), message, int(hour), int(min), 15, True, 2)

#Função que inicia toda interface
def main():
  app = wx.App()
  ex = Example(None, title='Lista de contatos')
  ex.Show()
  app.MainLoop()

if __name__ == '__main__':
  main()