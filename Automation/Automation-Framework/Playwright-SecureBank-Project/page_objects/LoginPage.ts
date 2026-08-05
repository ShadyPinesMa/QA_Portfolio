import { type Page, type Locator, expect } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly username: Locator
  readonly password: Locator
  readonly loginButton: Locator
  readonly error: Locator

  constructor(page: Page) {
    this.page = page
    this.username = page.getByTestId('login-username-input')
    this.password = page.getByTestId('login.password-input')
    this.loginButton = page.getByTestId('login-submit-btn')
    this.error = page.getByTestId('login-error-message')
  }

  async goto() {
    await this.page.goto('/')
  }

  async login(user: string, pass: string) {
    await this.username.fill(user)
    await this.password.fill(pass)
    await this.loginButton.click()
  }

  async expectLoggedIn() {
    await expect(this.page).toHaveURL(/dashboard/)
  }

  async expectError(message: string | RegExp) {
    await expect(this.error).toContainText(message)
  }
}
