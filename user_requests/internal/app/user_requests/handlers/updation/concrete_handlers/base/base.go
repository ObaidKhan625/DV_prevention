package base

import (
	"context"
	"fmt"
	sq "github.com/Masterminds/squirrel"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/pkg/postgres"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type BaseHandler struct {
	input Input
}

func (b BaseHandler) HandleRequest(w http.ResponseWriter, r *http.Request) {
	b.SetResponseOnWriter(w)

	recipientUserId := r.URL.Query().Get("user_id")

	currentUserId := "1"

	if currentUserId == recipientUserId || b.inputHasInvalidData() {
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	reportExists := b.ExistsInDB(conn)
	if reportExists {
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	err = b.AddToDB(conn)
	fmt.Println("Insert error : ", err)
}

func (b BaseHandler) ExistsInDB(conn *pgx.Conn) bool {
	queryEq := sq.Eq{}
	for columnName, columnValue := range b.input.ColumnDataMap {
		queryEq[columnName] = columnValue
	}

	reportExistsSQL :=
		sq.Select("1").
			From(b.input.TableName).
			Where(queryEq).
			PlaceholderFormat(sq.Dollar).
			Limit(1)

	return postgres.CheckIfRecordsExist(reportExistsSQL, conn)
}

func (b BaseHandler) AddToDB(conn *pgx.Conn) error {
	var columnNames []string
	var columnValues []any
	for columnName, columnValue := range b.input.ColumnDataMap {
		columnNames = append(columnNames, columnName)
		columnValues = append(columnValues, columnValue)
	}

	psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
	insertBuilder := psql.Insert(b.input.TableName).
		Columns(columnNames...).
		Values(columnValues...)
	return postgres.ExecInsertQueryFromBuilder(insertBuilder, conn)
}

func (b BaseHandler) GetFromDB() []handlers.UserRequestHandler {
	return []handlers.UserRequestHandler{}
}

func (b BaseHandler) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNoContent)
}

func (b BaseHandler) SetResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
}

func (b BaseHandler) inputHasInvalidData() bool {
	// todo: later on will have to check if something exists in the DB, rather than doing this
	for _, value := range b.input.ColumnDataMap {
		if value == "" {
			return true
		}
	}
	return false
}

func NewBaseHandler(input Input) *BaseHandler {
	return &BaseHandler{
		input: input,
	}
}
