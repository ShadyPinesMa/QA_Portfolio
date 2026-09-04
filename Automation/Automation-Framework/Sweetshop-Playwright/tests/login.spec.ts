import { test, expect } from '@playwright/test'
import { LoginPage } from '../pages/LoginPage'

test('valid login', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.open()

  await loginPage.login('oneorder@sweetshop.local', 'abcdefg')

  await loginPage.expectLoggedInAs('oneorder@sweetshop.local')
})

test('missing password', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.open()

  await loginPage.login('oneorder@sweetshop.local', '')

  await expect(page.getByText('Please enter a valid password')).toBeVisible()
})

test('valid login for two orders account', async ({ page }) => {
  const loginPage = new LoginPage(page)
  await loginPage.open()

  await loginPage.login('twoorders@sweetshop.local', 'abcdefg')

  await loginPage.expectLoggedInAs('twoorders@sweetshop.local')
})
