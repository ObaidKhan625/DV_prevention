package base

import (
	"context"
	"encoding/json"
	"fmt"
	sq "github.com/Masterminds/squirrel"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/pkg/postgres"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type BaseHandler struct {
	input Input
}

func (b BaseHandler) HandleRequest(w http.ResponseWriter, r *http.Request) {
	currentUserId := "1"

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	responseList, err := b.getDataFromDB(currentUserId, conn)
	fmt.Println(responseList)

	fmt.Println("Select error : ", err)
}

func (b BaseHandler) getDataFromDB(currentUserId string, conn *pgx.Conn) ([]string, error) {
	psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
	selectBuilder := psql.Select("requesting_user_id").
		From(b.input.TableName).
		Where(sq.Eq{"requested_user_id": currentUserId})

	var data []string
	data, err := postgres.GetRowsFromSelectBuilder(selectBuilder, conn)
	if err != nil {
		return []string{}, err
	}
	return data, err
}

func (b BaseHandler) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNoContent)
}

func (b BaseHandler) SetResponseOnWriter(w http.ResponseWriter, data any) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
	w.WriteHeader(http.StatusOK)
}

func NewBaseHandler(input Input) *BaseHandler {
	return &BaseHandler{
		input: input,
	}
}
