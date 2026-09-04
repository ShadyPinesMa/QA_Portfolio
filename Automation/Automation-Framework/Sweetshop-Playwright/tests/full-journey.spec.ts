import { test, expect } from '@playwright/test'
import { HomePage } from '../pages/HomePage'
import { BasketPage } from '../pages/BasketPage'
import { ProductPage } from '../pages/ProductPage'

test('add products to basket, verify item count on basket page, complete checkout', async ({
  page,
}) => {
  const homePage = new HomePage(page)
  const basketPage = new BasketPage(page)
  const productPage = new ProductPage(page)

  await homePage.open()
  await homePage.goToProducts()

  await expect(productPage.productHeader).toBeVisible()

  await productPage.addProductToBasket('Wham Bar')
  await productPage.addProductToBasket('Strawberry Bon Bons')

  await basketPage.open()
  expect(await basketPage.getBasketCount()).toBe(2)

  await basketPage.fillCheckoutForm()
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Thank you!')).toBeVisible()
})
