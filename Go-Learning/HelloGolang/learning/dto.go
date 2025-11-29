package learning

import "fmt"

type Account struct {
	Id       string
	Name     string
	Password string
}

// Id 或 Name 登录判断

func (account *Account) CheckPassword(id, name, password string) map[string]string {
	if id != account.Id && name != account.Name {
		return map[string]string{"code": "401", "msg": "Account Not Found"}
	}
	flag := (id == "" && name == account.Name && password == account.Password) || (id == account.Id && password == account.Password)
	if flag {
		return map[string]string{"code": "200", "msg": "Login Success"}
	}
	return map[string]string{"code": "400", "msg": "Login Failed, Wrong PWD"}
}

func (account *Account) ChangePassword(id, name, password, newPassword string) bool {
	if account.Id == id && account.Name == name && account.Password == password {
		account.Password = newPassword
		return true
	}
	return false
}

func TestDto() {
	account := Account{Id: "1", Name: "test", Password: "123456"}
	fmt.Println(account)
	fmt.Println(account.CheckPassword("", "test1", "123456"))
}
