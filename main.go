package main

import (
	"net/http"
	"stock/handler"
)

func main() {
	staticDir := http.FileServer(http.Dir("static"))
	csvDir := http.FileServer(http.Dir("d:/stock"))
	http.Handle("/static/", http.StripPrefix("/static/", staticDir))
	http.Handle("/csv/", http.StripPrefix("/csv/", csvDir))
	http.HandleFunc("/search", handler.Search)
	if err := http.ListenAndServe(":8991", nil); err != nil {
		panic(err)
	}
}
