# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_ByjobAndNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-12-21 14:36:20.210000
- **Ngày sửa cuối**: 2022-12-21 14:36:20.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@p_ID` | `int(4)` | No |
| `@p_NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_job]
create PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ByjobAndNgayThucHien]
	-- Add the parameters for the stored procedure here
	@p_ID INT,
	@p_NgayThucHien DATETIME
AS
BEGIN
	
	

	DECLARE @ID INT = 0
	DECLARE @JobID INT
	DECLARE @NgayThucHien DATETIME = NULL
	--SET @NgayThucHien = '2018-01-13'
	
	SET @ID = @p_ID
	SET @NgayThucHien = @p_NgayThucHien

	DECLARE icursor CURSOR FOR   
		SELECT DISTINCT Id
		FROM RecurringJobs.dbo.JOBS_LOG 
		WHERE CONVERT(DATE, DateExecute) = CONVERT(DATE, GETDATE())
				AND Status = 1
				AND Id IN (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 58, 59, 60, 61, 63,65,66,67,68,69,70,71,72,73,74, 75,76,83,84,85)
		ORDER BY Id
	
	OPEN icursor  
	
	FETCH NEXT FROM icursor   
	INTO @JobID
	
	WHILE @@FETCH_STATUS = 0  
	BEGIN  
		-- Do du lieu cho các sp:
		--		Banner_CPD_by_Contract
		--		BoxApp CPD by Contract
		--		CPM Chuyen trang
		--		Balloon Ads
		--		TVC
		--		Boxapp CPM
		--		Mobile
		--		King Size
		--		CPM Stick
		--		Brand Page
		--		Content Network Sponsorship
		--		Sponsor
		--		Native asd chay theo ngay


		IF @JobID IN (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 59, 61,74,84)
			BEGIN
				IF @JobID IN (22,60) --CPD tool cp cu
					BEGIN
						SET @ID = -3
					END
				IF @JobID = 23 -- CPD tool cp cu
					BEGIN
						SET @ID = -2
					END
				IF @JobID = 25
					BEGIN
						SET @ID = 5
					END
				IF @JobID = 26
					BEGIN
						SET @ID = 8
					END
				IF @JobID = 27
					BEGIN
						SET @ID = 9
					END
				IF @JobID = 28
					BEGIN
						SET @ID = 10
					END
				IF @JobID = 29
					BEGIN
						SET @ID = 14
					END
				IF @JobID = 30
					BEGIN
						SET @ID = 15
					END
				IF @JobID = 31
					BEGIN
						SET @ID = 16
					END
				IF @JobID = 32
					BEGIN
						SET @ID = 17
					END
				IF @JobID = 33
					BEGIN
						SET @ID = 18
					END
				IF @JobID = 59
					BEGIN
						SET @ID = 5056
					END
				IF @JobID = 61
					BEGIN
					    SET @ID = 19
					END
				IF @JobID = 74 --CPD tool cp moi
					BEGIN
					    SET @ID = 1
					END
				IF @JobID = 84 --Audio ads
					BEGIN
					    SET @ID = 5299
					END
				PRINT 'CPM'
			    EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 1, @NgayThucHien
			END


		-- lấy report UV (CPR) cho các sản phẩm
		--lấy report UV (CPR) cho các sản phẩm
		--lấy report UV (CPR) cho các sản phẩm
		IF @JobID IN (34, 35, 40)
			BEGIN
			    IF @JobID = 34
					BEGIN
						SET @ID = 14
					END
				IF @JobID = 35
					BEGIN
						SET @ID = 16
					END
				IF @JobID = 40
					BEGIN
						SET @ID = 18
					END
				PRINT 'CPR'
				EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 2, @NgayThucHien
			END

		-- lấy report CPV cho TVC
		IF @JobID IN (36)
			BEGIN
				SET @ID = 9999
				PRINT 'TVC'
				EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 3, @NgayThucHien
			END

		-- lấy report True View
		IF @JobID IN (37)
			BEGIN
				SET @ID = 9999
				PRINT 'True View'
				EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 4, @NgayThucHien
			END

		-- lấy report thực chạy sản phẩm boxapp selfserving
		IF @JobID IN (38)
			BEGIN
				SET @ID = 9999
				PRINT 'Box app selfserving'
				EXEC dbo.ThucChay_DoDuLieuTuAPIVaoBang @ID, 5, @NgayThucHien
			END
	    
		-- lấy report thực chạy sản phẩm native ads day vao table ThucChay_Native_ads
		IF @JobID IN (58)
		BEGIN
			SET @ID = 19
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads] 
			 @NgayThucHien = @NgayThucHien,
			 @TypeProduct = @ID
		END
		-- Lay thong tin thuc chay on OnImageAds day vao table ThucChay_Native_ads
		IF @JobID IN (63)
		BEGIN
			SET @ID = 5133
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Native_ads_From_OnImageAds] 
			 @NgayThucHien = @NgayThucHien,
			 @TypeProduct = @ID
		END
		--************ Lay thong tin thuc chay thanh tien admatic day vao table ThucChay_ThanhTien_Admatic ************----------
		IF @JobID IN (65)--Balloon
		BEGIN
			SET @ID = 339 --Balloon
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
		IF @JobID IN (66)--TVC online
		BEGIN
			SET @ID = 240 --TVC Online
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (67)--Boxapp CPM
		BEGIN
			SET @ID = 370 --Boxapp CPM
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (68)--Mobile
		BEGIN
			SET @ID = 342 --Mobile
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (69)--KingSize
		BEGIN
			SET @ID = 598 --KingSize
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (70)--CPM Stick
		BEGIN
			SET @ID = 613 --CPM Stick
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (71)--Brand Page
		BEGIN
			SET @ID = 680 --Brand Page
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (72)--Sponsor Page
		BEGIN
			SET @ID = 735 --Sponsor Page
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END

		IF @JobID IN (73)--Adx
		BEGIN
			SET @ID = 585 --Adx
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
		IF @JobID IN (75)--Native ads
		BEGIN
			SET @ID = 821 --Native ads
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
		IF @JobID IN (76)--On image
		BEGIN
			SET @ID = 5133 --On image
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
		--5056
		IF @JobID IN (83)--Box Gallery
		BEGIN
			SET @ID = 5056 --Box Gallery
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
		--5268
		IF @JobID IN (85)--Brand Lift Survey
		BEGIN
			SET @ID = 5268 --Brand Lift Survey
			print @id
			EXEC [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_ThucChay_ThanhTien_Admatic] 
			 @NgayThucHien = @NgayThucHien,
			 @DmSanPhamREF = @ID
		END
	    FETCH NEXT FROM icursor   
	    INTO @JobID 
	END   
	CLOSE icursor;  
	DEALLOCATE icursor;  

END


```
