package handler

import (
	"fmt"
	"net/http"
	"os"
	"text/template"
	"time"
)

var tmpl = template.Must(template.ParseFiles("static/index.html"))

func Search(w http.ResponseWriter, r *http.Request) {
	//form := r.ParseForm()
	d := r.FormValue("d")
	n := r.FormValue("n")
	if len(d) == 0 {
		d = time.Now().Format("2006-01-02")
	}
	if len(n) == 0 {
		n = "list"
	}
	f := fmt.Sprintf("%s/%s_%s.csv", d, n, d)
	_, err := os.Stat("d:/stock/" + f)
	if os.IsNotExist(err) {
		w.Write([]byte("d:/stock/" + f + " 不存在"))
	} else if err != nil {
		w.Write([]byte(err.Error()))
	} else {
		f = "csv/" + f
		tmpl.ExecuteTemplate(w, "Index", struct {
			CsvPath string
			Kind    string
			Date    string
		}{f, n, d})
	}
}
