package postgres

import (
	"context"
	"errors"
	sq "github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v5"
)

func ExecQueryFromBuilder(insertBuilder sq.InsertBuilder, conn *pgx.Conn) error {
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
