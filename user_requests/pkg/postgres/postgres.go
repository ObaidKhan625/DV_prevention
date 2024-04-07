package postgres

import (
	"context"
	"errors"
	sq "github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v5"
)

func ExecInsertQueryFromBuilder(insertBuilder sq.InsertBuilder, conn *pgx.Conn) error {
	sql, args, _ := insertBuilder.ToSql()

	_, err := conn.Exec(context.Background(),
		sql,
		args...,
	)
	return err
}

func CheckIfRecordsExist(selectBuilder sq.SelectBuilder, conn *pgx.Conn) bool {
	sql, args, _ := selectBuilder.ToSql()

	resultFlag := 0
	err := conn.QueryRow(context.Background(), sql, args...).Scan(&resultFlag)
	if err != nil && errors.Is(err, pgx.ErrNoRows) {
		return false
	}
	return true
}

func GetRowsFromSelectBuilder(selectBuilder sq.SelectBuilder, conn *pgx.Conn) ([]string, error) {
	sql, args, _ := selectBuilder.ToSql()
	rows, err := conn.Query(context.Background(), sql, args...)
	if err != nil {
		return []string{}, err
	}

	data := make([]string, 0)
	for rows.Next() {
		var val string
		err = rows.Scan(&val)
		if err != nil {
			return nil, err
		}
		data = append(data, val)
	}

	return data, nil
}
