package serve

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"net/http"
)

func ServeRequest(w http.ResponseWriter, r *http.Request, handler handlers.UserRequestHandler) {
	//body, err := io.ReadAll(r.Body)
	//if err != nil {
	//	http.Error(w, "Failed to read request body", http.StatusBadRequest)
	//	return
	//}

	handler.HandleRequest(w, r)

	//var creds credentials
	//err = json.Unmarshal(body, &creds)
	//if err != nil {
	//	http.Error(w, "Failed to parse JSON body", http.StatusBadRequest)
	//	return
	//}
	//
	//jsonResponse, err := json.Marshal(creds)
	//if err != nil {
	//	http.Error(w, "Failed to marshal JSON response", http.StatusInternalServerError)
	//	return
	//}
	//
	//w.Header().Set("Content-Type", "application/json")
	//w.WriteHeader(http.StatusOK)
	//_, _ = w.Write(jsonResponse)
}
