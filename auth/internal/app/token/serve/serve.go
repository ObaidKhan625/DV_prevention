package serve

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/app/token/handlers"
	"io"
	"net/http"
)

func ServeRequest(w http.ResponseWriter, r *http.Request, handler handlers.TokenHandler) {
	_, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Failed to read request body", http.StatusBadRequest)
		return
	}
	handler.HandleRequest(w, r)
}
