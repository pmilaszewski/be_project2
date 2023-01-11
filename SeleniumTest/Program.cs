using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

#region Variable setup

var options = new ChromeOptions();
options.AddArgument("--ignore-ssl-errors=yes");
options.AddArgument("--ignore-certificate-errors");
options.AddArguments("--disable-infobars");

var name = "Harry";
var surname = "Potter";
var email = "harrypotter" + Guid.NewGuid().ToString() + "@wp.pl";
var password = "zaq1@WSX";
var dateOfBirth = "1998-09-27";
var address = "Przekatna";
var postCode = "82-200";
var city = "Londyn";

#endregion

using (var driver = new ChromeDriver(".", options))
{
    driver.Navigate().GoToUrl($"https://localhost/pl/");

    #region Add 10 products to basket
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/a")).Click();

    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div[1]/div[1]/ul/li[2]/ul/li[3]/a")).Click();

    for(int i = 1; i < 9; i++)
    {
        Thread.Sleep(500);
        driver.FindElement(By.XPath("html/body/main/section/div/div[2]/section/section/div[3]/div/div[1]/article[" + i +"]/div/a/img")).Click();
        
        var rand = new Random();
        for(int j = 1; j < rand.Next(1, 4); j++)
        {
            Thread.Sleep(500);
            driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/span[3]/button[1]/i")).Click();
        }
        
        Thread.Sleep(500);
        driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button")).Submit();

        Thread.Sleep(500);
        driver.FindElement(By.XPath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/button")).Click();
        Thread.Sleep(500);
        driver.Navigate().GoToUrl($"https://localhost/pl/148-czarne-kinkiety");
    }
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div[1]/div[1]/ul/li[2]/ul/li[20]/a")).Click();
    
    for(int i = 1; i < 3; i++)
    {
        Thread.Sleep(500);
        driver.FindElement(By.XPath("html/body/main/section/div/div[2]/section/section/div[3]/div/div[1]/article[" + i +"]/div/a/img")).Click();
        var rand = new Random();
        for(int j = 1; j < rand.Next(1, 4); j++)
        {
            Thread.Sleep(500);
            driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/span[3]/button[1]/i")).Click();
        }
        Thread.Sleep(500);
        driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button")).Submit();

        Thread.Sleep(500);
        driver.FindElement(By.XPath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/button")).Click();
        Thread.Sleep(500);
        driver.Navigate().GoToUrl($"https://localhost/pl/12-lampy-biurkowe");
    }
    
    #endregion

    #region Remove item from basket
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/header/nav/div/div/div[1]/div[2]/div[3]/div/div/a/span[1]")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[3]/div/a/i")).Click();
    

    #endregion

    #region Register new user 
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/a/span")).Click();
    
    Thread.Sleep(500);
    driver.FindElement(By.XPath("html/body/main/section/div/div/section/section/div/a")).Click();

    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[1]/div[1]/label[1]/span/input")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("html/body/main/section/div/div/section/section/section/form/section/div[2]/div[1]/input")).SendKeys(name);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[3]/div[1]/input")).SendKeys(surname);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[4]/div[1]/input")).SendKeys(email);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[5]/div[1]/div/input")).SendKeys(password);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("html/body/main/section/div/div/section/section/section/form/section/div[6]/div[1]/input")).SendKeys(dateOfBirth);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[7]/div[1]/span/label/input")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/section/div[8]/div[1]/span/label/input")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/section/form/footer/button")).Click();

    #endregion

    #region Handle basket

    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/header/nav/div/div/div[1]/div[2]/div[3]/div")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/div/div[2]/div[1]/div[2]/div/a")).Click();


    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[2]/div/div/form/div/div/section/div[5]/div[1]/input")).SendKeys(address);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[2]/div/div/form/div/div/section/div[7]/div[1]/input")).SendKeys(postCode);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[2]/div/div/form/div/div/section/div[8]/div[1]/input")).SendKeys(city);
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[2]/div/div/form/div/div/footer/button")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("//*[@id=\"delivery_option_10\"]")).Click();    
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[3]/div/div[2]/form/button")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[4]/div/div[2]/div[4]/div/span")).Click();
    Thread.Sleep(500);


    driver.FindElement(By.XPath("//*[@id=\"conditions_to_approve[terms-and-conditions]\"]")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/section/div/section/div/div[1]/section[4]/div/div[3]/div[1]/button")).Click();

    #endregion

    #region Check order
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/a[2]/span")).Click();
    Thread.Sleep(500);
    driver.FindElement(By.XPath("/html/body/main/section/div/div/section/section/div/div/a[3]/span/i")).Click();
    #endregion

    Thread.Sleep(50000);
}