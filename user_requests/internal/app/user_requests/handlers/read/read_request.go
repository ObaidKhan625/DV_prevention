package read

import (
	"net/http"
)

type ReadRequest interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
	SetUnsuccessfulResponseOnWriter(w http.ResponseWriter)
	SetResponseOnWriter(w http.ResponseWriter, data any)
}
