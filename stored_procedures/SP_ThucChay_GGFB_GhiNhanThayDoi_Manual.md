# Stored Procedure: `ThucChay_GGFB_GhiNhanThayDoi_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-27 11:38:40.437000
- **Ngày sửa cuối**: 2025-10-27 11:52:36.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql


--EXEC [dbo].[ThucChay_GGFB_GhiNhanThayDoi]
--	@NgayGhiNhan = '2025-04-18',
--	@NgayCheckThayDoi  = '2025-04-18',
--	@NgayDanhSoGioiHan  = '2022-04-18'
--	--@SoHopDong = '2025-04-18',
--	--@HopDongChiTietID  = NULL
/*
exec [dbo].[ThucChay_GGFB_GhiNhanThayDoi_Manual]
	@NgayGhiNhan = '2025-10-25',
	@NgayCheckThayDoi =  '2025-10-25',
	@SoHopDong = N'MA1101025',
	@HopDongChiTietID = 768139
*/



CREATE PROCEDURE [dbo].[ThucChay_GGFB_GhiNhanThayDoi_Manual]
	@NgayGhiNhan DATE,
	@NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	--================================= TH chạy lại SP từ lần thứ 2 trong cùng @NgayGhiNhan
	-- Không cần update lại iscalculate của bảng [ADS_Operating_Result_Quantity] và [ADS_Operating_Result_Map_Order] 
	-- vì các xử lý sau ko quan tâm đến trường thông tin này

	DELETE tcdt
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayGhiNhan AND 
		  tcdt.DotChayHopDong = N'Tính thay đổi GGFB' AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	DELETE tcdt
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh_MuaNgoai tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayGhiNhan AND 
		  tcdt.ghichu LIKE N'Ghi nhận thay đổi%' 
		  AND (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) 
          AND (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 


	CREATE TABLE #dmIDtinhmoi (ID INT, type INT)

	INSERT INTO #dmIDtinhmoi
	SELECT tcdt.DotChayBooking, 
		   IIF(tcdt.DotChayHopDong = N'Tính mới GGFB result_map_order', 1, 2)
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayGhiNhan AND 
		  tcdt.DotChayHopDong IN (N'Tính mới GGFB result_map_order', N'Tính mới GGFB result_quantity') AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	--=================================================== Xác định danh mục phân bổ cần xử lý thay đổi =====================================

	CREATE TABLE #DmPBThayDoi
	(		 HopDongID INT,
			 HopDongChiTietID INT,
			 OrderID INT,
			 OperatorID INT,
			 ResultID INT,
			 IsActive_hdct INT,
			 IsActive_Order INT,
			 IsActive_Operator INT,
			 Operator_Type INT,  
			 --1: kết quả vân hành hàng ngày
			 --2: vận hành chốt
			 LoaiThayDoi INT,
			 --1/2: Order thay đổi phân bổ => phân bổ trước sau, pb nào active thì đối trừ tính lại
			 --3/4: vận hành đổi order ở 2 phân bổ khác nhau => phân bổ trước sau, pb nào active thì đối trừ tính lại
			 --5: phân bổ/ hợp đồng hủy => đối trừ phân bổ
			 --6: phân bổ giảm giá trị, thay đổi chiết khấu => đối trừ tính lại phân bổ  
			 --7: Order hủy, thay đổi ngân sách => đối trừ tính lại phân bổ
			 --8: vận hành hủy, thay đổi thành tiền, số lượng, order => đối trừ tính lại phân bổ
			 --9: ADS_Operating_Result thay đổi TT hoặc [ADS_Operating_Result_Map_Order] thay đổi result_id => thay đổi thành tiền mua của order => tính lại lãi
			 LoaiXuLy INT,
			 --1: đối trừ thucchaydatinh và thucchaydatinh_muangoai của cả phân bổ
			 --2: đối trừ tính lại thucchaydatinh và thucchaydatinh_muangoai của cả phân bổ
			 LyDo NVARCHAR(MAX)
	)
	--===========1/2: order thay đổi phân bổ: cả 2 phân bổ trước và sau đều active hoặc 1 trong 2 phân bổ active
	BEGIN
		INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,IsActive_hdct
			,IsActive_Order 
			,LoaiThayDoi
			,LoaiXuLy )
		SELECT DISTINCT
			   ISNULL(hd.HopDongID, 0),
			   ISNULL(OD.Contract_Detail_Id, 0),  -- phân bổ hiện tại
			   OD.ID,
			   IIF(ISNULL(OD.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1),
			   OD.IsDeleted,
			   1,
			   2
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Order OD 
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE CONVERT(date,OD.LastModificationTime) = @NgayCheckThayDoi
			  --AND CONVERT(date,OD.CreationTime) < @NgayCheckThayDoi
			  AND @SoHopDong IS NULL 

		INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,IsActive_hdct
			,IsActive_Order
			,LoaiThayDoi
			,LoaiXuLy  )
		SELECT DISTINCT
			   hd.HopDongID
			  ,ISNULL(L.Contract_Detail_Id, 0)   -- phân bổ before
			  ,dm.OrderID
			  ,IIF(ISNULL(L.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1)
			  ,dm.IsActive_Order
			  ,2
			  ,2
		FROM #DmPBThayDoi dm
		OUTER APPLY (SELECT TOP 1 L.Contract_Detail_Id, L.IsDeleted
					 FROM dbo.ADS_Operating_Order_Log L  
					 WHERE CAST(L.LastModificationTime AS DATE) < @NgayCheckThayDoi AND 
						   dm.OrderID = L.ADS_Operating_Order_Id
					 ORDER BY L.LastModificationTime DESC ) L
		LEFT JOIN ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON L.Contract_Detail_Id = hdct.HopDongChiTietID
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE dm.LoaiThayDoi = 1  

		UPDATE dm
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm
		LEFT JOIN #DmPBThayDoi dm2 ON  dm.LoaiThayDoi = 2 AND 
									   dm.OrderID = dm2.OrderID
		WHERE dm.LoaiThayDoi = 1 AND
			 (dm.IsActive_hdct = 0 OR							-- TH phân bổ sau không active
			  dm.HopDongChiTietID = dm2.HopDongChiTietID OR		-- TH phân bổ trước và sau không TĐ
			  dm.IsActive_Order = 0 )							-- TH tại thời điểm hiện tại, order bị hủy		

		UPDATE dm2
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm2
		LEFT JOIN #DmPBThayDoi dm  ON  dm.LoaiThayDoi = 1 AND 
									   dm.OrderID = dm2.OrderID
		WHERE dm2.LoaiThayDoi = 2 AND
			 (dm2.IsActive_hdct = 0 OR							-- TH phân bổ trước TĐ không active
			  dm2.HopDongChiTietID = dm.HopDongChiTietID OR		-- TH phân bổ trước và sau không TĐ
			  dm2.IsActive_Order = 0 )							-- TH tại thời điểm hiện tại, order bị hủy	
		  
		DELETE
		FROM #DmPBThayDoi
		WHERE LoaiXuLy = 0

		UPDATE dm
		SET Lydo = N'order ' + pb_orders.OrderList + N' được chuyển vào phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(OrderID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 1
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OrderList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 1
				GROUP BY dm1.HopDongChiTietID
			) pb_orders ON dm.HopDongChiTietID = pb_orders.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 1

		UPDATE dm
		SET Lydo = N'order ' + pb_orders.OrderList + N' bị gỡ ra khỏi phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(OrderID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 2
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OrderList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 2
				GROUP BY dm1.HopDongChiTietID
			) pb_orders ON dm.HopDongChiTietID = pb_orders.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 2

	END

	--================3/4: Vận hành đổi order ở 2 phân bổ khác nhau: cả 2 phân bổ trước và sau đều active hoặc 1 trong 2 phân bổ active
	BEGIN
		--a./ ADS_Operating_Result_Quantity thay đổi
		INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,OperatorID 
			,IsActive_hdct 
			,IsActive_Order 
			,IsActive_Operator 
			,Operator_Type
			,LoaiThayDoi
			,LoaiXuLy )
		SELECT DISTINCT
			   ISNULL(hd.HopDongID, 0),
			   ISNULL(OD.Contract_Detail_Id, 0),  -- phân bổ hiện tại
			   ISNULL(OD.ID, 0),
			   RQ.Id,
			   IIF(ISNULL(OD.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1),
			   IIF(ISNULL(RQ.Operating_Order_Id, 0) = 0 OR OD.IsDeleted = 1, 0, 1),
			   IIF(RQ.IsDeleted = 1, 0, 0),
			   2,
			   3,
			   2
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Quantity RQ 
		LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.Id = RQ.Operating_Order_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE CONVERT(date,RQ.LastModificationTime) = @NgayCheckThayDoi
			  --AND CONVERT(date,RQ.CreationTime) < @NgayCheckThayDoi
			  AND RQ.IsCalc_Result_Quantity = 1
			  AND @SoHopDong IS NULL 

		INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,OperatorID 
			,IsActive_hdct 
			,IsActive_Order 
			,IsActive_Operator 
			,Operator_Type
			,LoaiThayDoi
			,LoaiXuLy )
		SELECT DISTINCT
			   hd.HopDongID
			  ,ISNULL(OD.Contract_Detail_Id, 0)   -- phân bổ before
			  ,dm.OrderID
			  ,dm.OperatorID
			  ,IIF(ISNULL(OD.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1)
			  ,IIF(ISNULL(L.Operating_Order_Id, 0) = 0 OR OD.IsDeleted = 1, 0, 1)
			  ,dm.IsActive_Operator
			  ,2
			  ,4
			  ,2
		FROM #DmPBThayDoi dm
		OUTER APPLY (SELECT TOP 1 L.Operating_Order_Id, L.IsDeleted
					 FROM dbo.ADS_Operating_Result_Quantity_log L 
					 WHERE CAST(L.LastModificationTime AS DATE) < @NgayCheckThayDoi AND 
						   dm.OperatorID = L.ADS_Operating_Result_Quantity_Id
					 ORDER BY L.LastModificationTime DESC ) L
		LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.Id = L.Operating_Order_Id
		LEFT JOIN ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE dm.LoaiThayDoi = 3 AND Operator_Type = 2

		UPDATE dm
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm
		LEFT JOIN #DmPBThayDoi dm2 ON  dm2.LoaiThayDoi = 4 AND 
									   dm2.Operator_Type = 2 AND 
									   dm2.OperatorID = dm.OperatorID
		WHERE dm.LoaiThayDoi = 3 AND dm.Operator_Type = 2 AND 
			 (dm.IsActive_hdct = 0 OR							-- TH phân bổ sau không active
			  dm.HopDongChiTietID = dm2.HopDongChiTietID OR		-- TH phân bổ trước và sau không TĐ
			  dm.IsActive_Order = 0 OR 							-- TH tại thời điểm hiện tại, order bị hủy	
			  dm.IsActive_Operator = 0)							-- TH tại thời điểm hiện tại, vận hành bị hủy

		UPDATE dm2
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm2
		LEFT JOIN #DmPBThayDoi dm ON   dm.LoaiThayDoi = 3 AND 
									   dm.Operator_Type = 2 AND 
									   dm.OperatorID = dm2.OperatorID 
		WHERE dm2.LoaiThayDoi = 4 AND dm2.Operator_Type = 2 AND 
			 (dm2.IsActive_hdct = 0 OR							-- TH phân bổ trước TĐ không active
			  dm2.HopDongChiTietID = dm.HopDongChiTietID OR 	-- TH phân bổ trước và sau không TĐ
			  dm2.IsActive_Order = 0 OR							-- TH Order trước thay đổi không active
			  dm2.IsActive_Operator = 0)						-- TH tại thời điểm hiện tại, vận hành bị hủy
		  
		DELETE
		FROM #DmPBThayDoi
		WHERE LoaiXuLy = 0


		--b./ ADS_Operating_Result_Map_Order thay đổi
		INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,OperatorID 
			,IsActive_hdct 
			,IsActive_Order 
			,IsActive_Operator 
			,Operator_Type
			,LoaiThayDoi
			,LoaiXuLy)
		SELECT DISTINCT
			   ISNULL(hd.HopDongID, 0),
			   ISNULL(OD.Contract_Detail_Id, 0),  -- phân bổ hiện tại
			   ISNULL(OD.ID, 0),
			   MP.Id,
			   IIF(ISNULL(OD.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1),
			   IIF(ISNULL(MP.Operating_Order_Id, 0) = 0 OR OD.IsDeleted = 1, 0, 1),
			   IIF(MP.IsDeleted = 1, 0, 0),
			   1,
			   3,
			   2
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Map_Order MP 
		LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.Id =MP.Operating_Order_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE CONVERT(date,MP.LastModificationTime) = @NgayCheckThayDoi
			  --AND CONVERT(date,MP.CreationTime) < @NgayCheckThayDoi
			  AND MP.IsCaculatedActual = 1
			  AND @SoHopDong IS NULL 

		INSERT INTO #DmPBThayDoi  
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,OperatorID 
			,IsActive_hdct 
			,IsActive_Order 
			,IsActive_Operator 
			,Operator_Type
			,LoaiThayDoi
			,LoaiXuLy)
		SELECT DISTINCT
			   hd.HopDongID
			  ,ISNULL(OD.Contract_Detail_Id, 0)   -- phân bổ before
			  ,dm.OrderID
			  ,dm.OperatorID
			  ,IIF(ISNULL(OD.Contract_Detail_Id ,0) = 0 OR hdct.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3, 0 , 1)
			  ,IIF(ISNULL(L.Operating_Order_Id, 0) = 0 OR OD.IsDeleted = 1, 0, 1)
			  ,dm.IsActive_Operator
			  ,1
			  ,4
			  ,2
		FROM #DmPBThayDoi dm
		OUTER APPLY (SELECT TOP 1 L.Operating_Order_Id, L.IsDeleted
					 FROM dbo.ADS_Operating_Result_Map_Order_Log L 
					 WHERE CAST(L.LastModificationTime AS DATE) < @NgayCheckThayDoi AND 
						   dm.OperatorID = L.ADS_Operating_Result_Map_Order_Id
					 ORDER BY L.LastModificationTime DESC ) L
		LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.Id = L.Operating_Order_Id
		LEFT JOIN ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
		LEFT JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE dm.LoaiThayDoi = 3 AND Operator_Type = 1

		SELECT * FROM #DmPBThayDoi

		UPDATE dm
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm
		LEFT JOIN #DmPBThayDoi dm2 ON  dm2.LoaiThayDoi = 4 AND 
									   dm2.Operator_Type = 1 AND 
									   dm2.OperatorID = dm.OperatorID
		WHERE dm.LoaiThayDoi = 3 AND dm.Operator_Type = 1 AND 
			 (dm.IsActive_hdct = 0 OR							-- TH phân bổ sau không active
			  dm.HopDongChiTietID = dm2.HopDongChiTietID OR		-- TH phân bổ trước và sau không TĐ
			  dm.IsActive_Order = 0 OR 							-- TH tại thời điểm hiện tại, order bị hủy	
			  dm.IsActive_Operator = 0)							-- TH tại thời điểm hiện tại, vận hành bị hủy

		UPDATE dm2
		SET LoaiXuLy = 0
		FROM #DmPBThayDoi dm2
		LEFT JOIN #DmPBThayDoi dm ON   dm.LoaiThayDoi = 3 AND 
									   dm.Operator_Type = 1 AND 
									   dm.OperatorID = dm2.OperatorID 
		WHERE dm2.LoaiThayDoi = 4 AND dm2.Operator_Type = 1 AND 
			 (dm2.IsActive_hdct = 0 OR							-- TH phân bổ trước TĐ không active
			  dm2.HopDongChiTietID = dm.HopDongChiTietID OR 	-- TH phân bổ trước và sau không TĐ
			  dm2.IsActive_Order = 0 OR							-- TH Order trước thay đổi không active
			  dm2.IsActive_Operator = 0)						-- TH tại thời điểm hiện tại, vận hành bị hủy
		  
		DELETE
		FROM #DmPBThayDoi
		WHERE LoaiXuLy = 0

		UPDATE dm
		SET Lydo = N'result_quantity ' + pb_operator.OperatorList + N' được chuyển ghi nhận thêm cho phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 3 AND 
								  dm2.Operator_Type = 2
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 3 AND dm1.Operator_Type = 2
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 3 AND dm.Operator_Type = 2

		UPDATE dm
		SET Lydo = N'result_quantity ' + pb_operator.OperatorList + N' bị gỡ không ghi nhận cho phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 4 AND 
								  dm2.Operator_Type = 2
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 4 AND dm1.Operator_Type = 2
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 4 AND dm.Operator_Type = 2


		UPDATE dm
		SET Lydo = N'result_map_order ' + pb_operator.OperatorList + N' được chuyển ghi nhận thêm cho phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 3 AND 
								  dm2.Operator_Type = 1
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 3 AND dm1.Operator_Type = 1
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 3 AND dm.Operator_Type = 1

		UPDATE dm
		SET Lydo = N'result_map_order ' + pb_operator.OperatorList + N' bị gỡ không ghi nhận cho phân bổ'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 4 AND 
								  dm2.Operator_Type = 1
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 4 AND dm1.Operator_Type = 1
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 4 AND dm.Operator_Type = 1

	END

	--============================5: hợp đồng, phân bổ xóa hủy => đối trừ phân bổ
	BEGIN
		INSERT INTO #DmPBThayDoi
			(    HopDongID
				,HopDongChiTietID 	
				,IsActive_hdct 
				,LoaiThayDoi
				,LoaiXuLy
				,LyDo   )
		SELECT DISTINCT
			   hd.HopDongID,
			   hdct.HopDongChiTietID,
			   0,
			   5,
			   1,
			   N'hợp đồng/ phân bổ hủy'
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Order OD 
		INNER JOIN ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE ((CONVERT(date,hd.LastModifiedAt) = @NgayCheckThayDoi AND (hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) ) OR
			   (CONVERT(date,hdct.LastModifiedAt) = @NgayCheckThayDoi AND hdct.DeletedStatus = 1))
			  AND OD.IsDeleted = 0
			  AND @SoHopDong IS NULL 

		IF @SoHopDong IS NOT NULL 
		BEGIN
			INSERT INTO #DmPBThayDoi
				(    HopDongID
					,HopDongChiTietID 	
					,IsActive_hdct 
					,LoaiThayDoi
					,LoaiXuLy
					,LyDo   )
			SELECT DISTINCT
				   hd.HopDongID,
				   hdct.HopDongChiTietID,
				   0,
				   5,
				   1,
				   N'xử lý tay hợp đồng/ phân bổ hủy'
			FROM ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct 
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE (hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1 OR hdct.DeletedStatus = 1)
				  AND hd.SoHopDong = @SoHopDong		
				  AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
		END
	END

	--==========================6: phân bổ giảm giá trị, thay đổi chiết khấu  => đối trừ tính lại phân bổ
	BEGIN
		INSERT INTO #DmPBThayDoi
			(    HopDongID
				,HopDongChiTietID 	
				,IsActive_hdct 
				,LoaiThayDoi
				,LoaiXuLy
				,LyDo   )
		SELECT DISTINCT
			   hd.HopDongID,
			   hdct.HopDongChiTietID,
			   1,
			   6,
			   2,
			   N'phân bổ thay đổi giá trị hoặc đổi chiết khấu'
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Order OD 
		INNER JOIN ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE CONVERT(date,hdct.LastModifiedAt) = @NgayCheckThayDoi 
			  AND OD.IsDeleted = 0
			  AND hdct.DeletedStatus = 0
			  AND hd.TrangThaiHopDong <> 3 AND hd.DeletedStatus = 0
			  --AND NOT EXISTS (SELECT dm.HopDongChiTietID
					--		  FROM #DmPBThayDoi dm
					--		  WHERE dm.HopDongChiTietID = hdct.HopDongChiTietID   )
			  AND @SoHopDong IS NULL 

		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN  ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct ON dm.HopDongChiTietID = hdct.HopDongChiTietID
		OUTER APPLY (SELECT TOP 1 L.ThanhTien, L.ChietKhau
					 FROM ABM_Data_ThucChay.dbo.HopDongChiTietLog L
					 WHERE CAST(L.LastModifiedAt AS DATE) < @NgayCheckThayDoi AND 
						   L.HopDongChiTietREF = hdct.HopDongChiTietID
					 ORDER BY L.LastModifiedAt desc) L
		WHERE dm.LoaiThayDoi = 6 AND
			( L.ThanhTien IS NULL  OR 
			 (hdct.ChietKhau = l.ChietKhau AND 
			  hdct.ThanhTien = L.ThanhTien) )

		IF @SoHopDong IS NOT NULL 
		BEGIN
			INSERT INTO #DmPBThayDoi
				(    HopDongID
					,HopDongChiTietID 	
					,IsActive_hdct 
					,LoaiThayDoi
					,LoaiXuLy
					,LyDo   )
			SELECT DISTINCT
				   hd.HopDongID,
				   hdct.HopDongChiTietID,
				   1,
				   6,
				   2,
				   N'xử lý tay phân bổ'
			FROM ABM_Data_ThucChay.[dbo].HopDongChiTiet hdct 
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3 AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0
				  AND hd.SoHopDong = @SoHopDong		
				  AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
		END
	END

	--=========================================7: Order hủy, thay đổi ngân sách => đối trừ tính lại phân bổ 
	INSERT INTO #DmPBThayDoi
	(    HopDongID
		,HopDongChiTietID 
		,IsActive_hdct
		,OrderID
		,IsActive_Order
		,LoaiThayDoi
		,LoaiXuLy
	)
	SELECT OD.HopDongID,
		   OD.HopDongChiTietID,
		   1,
		   OD.ID,
		   IIF(OD.IsDeleted = 1, 0, 1),
		   7,
		   2
	FROM (
			SELECT  DISTINCT
					hd.HopDongID,
					hdct.HopDongChiTietID,
					OD.ID,
					OD.IsDeleted,
					OD.Money_Turnover
			FROM ABM_Data_ThucChay.dbo.ADS_Operating_Order OD 
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE	CONVERT(date,OD.LastModificationTime) = @NgayCheckThayDoi
					--AND CONVERT(date,OD.CreationTime) < @NgayCheckThayDoi
					--AND OD.Contract_Detail_Id NOT IN (SELECT HopDongChiTietID
					--								FROM #DmPBThayDoi )
					AND hdct.DeletedStatus = 0 
					AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3
		  ) OD
	OUTER APPLY (SELECT TOP 1 L.Money_Turnover, L.IsDeleted, L.ID
				 FROM ABM_Data_ThucChay.dbo.ADS_Operating_Order_Log L
				 WHERE CAST(L.LastModificationTime AS DATE) < @NgayCheckThayDoi AND 
					   OD.ID = L.ADS_Operating_Order_Id 
				 ORDER BY L.LastModificationTime DESC) L
	WHERE @SoHopDong IS NULL  
		  AND ((OD.IsDeleted = 1 AND L.IsDeleted = 0) OR  ISNULL(OD.Money_Turnover, 0) <> ISNULL(L.Money_Turnover, 0))
		  AND L.ID IS NOT NULL 

	UPDATE dm
	SET Lydo = N'order ' + pb_order.OperatorList + N' thay đổi ngân sách'
	FROM #DmPBThayDoi dm
	JOIN (	SELECT dm1.HopDongChiTietID,
					STUFF((
						SELECT DISTINCT ',' + CAST(dm2.OrderID AS NVARCHAR(50))
						FROM #DmPBThayDoi dm2
						WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								dm2.LoaiThayDoi = 7 AND 
								dm2.IsActive_Order = 1
						FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
			FROM #DmPBThayDoi dm1
			WHERE dm1.LoaiThayDoi = 7 AND dm1.IsActive_Order = 1
			GROUP BY dm1.HopDongChiTietID
		) pb_order ON dm.HopDongChiTietID = pb_order.HopDongChiTietID
	WHERE dm.LoaiThayDoi = 7 AND dm.IsActive_Order = 1

	UPDATE dm
	SET Lydo = N'order ' + pb_order.OperatorList + N' bị hủy'
	FROM #DmPBThayDoi dm
	JOIN (	SELECT dm1.HopDongChiTietID,
					STUFF((
						SELECT DISTINCT ',' + CAST(dm2.OrderID AS NVARCHAR(50))
						FROM #DmPBThayDoi dm2
						WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								dm2.LoaiThayDoi = 7 AND 
								dm2.IsActive_Order = 0
						FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
			FROM #DmPBThayDoi dm1
			WHERE dm1.LoaiThayDoi = 7 AND dm1.IsActive_Order = 0
			GROUP BY dm1.HopDongChiTietID
		) pb_order ON dm.HopDongChiTietID = pb_order.HopDongChiTietID
	WHERE dm.LoaiThayDoi = 7 AND dm.IsActive_Order = 0

	--================================================8. result_quantity và result_map_order thay đổi tiền/số lượng/order_ID hoặc bị xóa
	BEGIN
		--a./ result_quantity
		INSERT INTO #DmPBThayDoi
			(    HopDongID
				,HopDongChiTietID 	
				,OrderID
				,OperatorID 
				,IsActive_hdct 
				,IsActive_Order 
				,IsActive_Operator 
				,Operator_Type
				,LoaiThayDoi
				,LoaiXuLy)
		SELECT	DISTINCT
				RQ.HopDongFK,
				RQ.Contract_Detail_Id,
				RQ.Operating_Order_Id,
				RQ.Id,
				1,
				1,
				IIF(ISNULL(RQ.IsDeleted, 0) = 0, 1, 0),
				2,
				8,
				2
		FROM (
				SELECT  RQ.id, RQ.IsDeleted, RQ.TotalMoney, RQ.Operating_Order_Id, RQ.Quantity, OD.Contract_Detail_Id, hdct.HopDongFK
				FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Quantity RQ
				INNER JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.ID = RQ.Operating_Order_Id
				INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
				INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				WHERE CONVERT(date,RQ.LastModificationTime) = @NgayCheckThayDoi
					  AND RQ.IsCalc_Result_Quantity = 1
					  --AND OD.Contract_Detail_Id NOT IN (SELECT HopDongChiTietID
							--							FROM #DmPBThayDoi )
					  AND hdct.DeletedStatus = 0 
					  AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3
				) RQ
		OUTER APPLY 
			 (
				SELECT TOP 1 L.IsDeleted, L.TotalMoney, L.Operating_Order_Id, L.Quantity
				FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Quantity_log L
				WHERE CONVERT(date,L.LastModificationTime) < @NgayCheckThayDoi
					  AND L.ADS_Operating_Result_Quantity_Id = RQ.Id
				ORDER BY L.LastModificationTime DESC 
				) L
		WHERE @SoHopDong IS NULL 
			  AND ((RQ.IsDeleted = 1 AND L.IsDeleted = 0) OR 
					ISNULL(RQ.TotalMoney, 0) <> ISNULL(L.TotalMoney, 0) OR 
					ISNULL(RQ.Operating_Order_Id, 0) <> ISNULL(L.Operating_Order_Id, 0) OR
					IIF(ISNULL(RQ.Quantity,0) = 0, 1, RQ.Quantity) <> IIF(ISNULL(L.Quantity,0) = 0, 1, L.Quantity)
				   )
			  AND L.IsDeleted IS NOT NULL

		--b./ result_map_order
		INSERT INTO #DmPBThayDoi
			(    HopDongID
				,HopDongChiTietID 	
				,OrderID
				,OperatorID 
				,IsActive_hdct 
				,IsActive_Order 
				,IsActive_Operator 
				,Operator_Type
				,LoaiThayDoi
				,LoaiXuLy  )
		SELECT	DISTINCT
				MP.HopDongFK,
				MP.Contract_Detail_Id,
				MP.Operating_Order_Id,
				MP.Id,
				1,
				1,
				IIF(ISNULL(MP.IsDeleted, 0) = 0, 1, 0),
				1,
				8,
				2
		FROM (
				SELECT  MP.id, MP.IsDeleted, MP.Sell_Money_VND, MP.Operating_Order_Id, MP.Result, OD.Contract_Detail_Id, hdct.HopDongFK
				FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Map_Order MP
				INNER JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.ID = MP.Operating_Order_Id
				INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
				INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				WHERE CONVERT(date,MP.LastModificationTime) = @NgayCheckThayDoi
					  AND MP.IsCaculatedActual = 1
					  --AND OD.Contract_Detail_Id NOT IN (SELECT HopDongChiTietID
							--							FROM #DmPBThayDoi )
					  AND hdct.DeletedStatus = 0 
					  AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3
				) MP
		OUTER APPLY 
			 (
				SELECT TOP 1 L.IsDeleted, L.Sell_Money_VND, L.Operating_Order_Id, L.Result
				FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Map_Order_Log L
				WHERE CONVERT(date,L.LastModificationTime) < @NgayCheckThayDoi
					  AND L.ADS_Operating_Result_Map_Order_Id = MP.Id
				ORDER BY L.LastModificationTime DESC 
				) L
		WHERE @SoHopDong IS NULL 
			  AND ((MP.IsDeleted = 1 AND L.IsDeleted = 0) OR 
					ISNULL(MP.Sell_Money_VND, 0) <> ISNULL(L.Sell_Money_VND, 0) OR 
					ISNULL(MP.Operating_Order_Id, 0) <> ISNULL(L.Operating_Order_Id, 0) OR
					IIF(ISNULL(MP.Result,0) = 0, 1, MP.Result) <> IIF(ISNULL(L.Result,0) = 0, 1, L.Result)
				   )
			  AND L.IsDeleted IS NOT NULL

		UPDATE dm
		SET Lydo = N'result_quantity ' + pb_operator.OperatorList + N' bị hủy hoặc thay đổi order/ thành tiền/ số lượng'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 8 AND 
								  dm2.Operator_Type = 2
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 8 AND dm1.Operator_Type = 2
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 8 AND dm.Operator_Type = 2

		UPDATE dm
		SET Lydo = N'result_map_order ' + pb_operator.OperatorList + N' bị hủy hoặc thay đổi order/ thành tiền/ số lượng'
		FROM #DmPBThayDoi dm
		JOIN (	SELECT dm1.HopDongChiTietID,
						STUFF((
							SELECT DISTINCT ',' + CAST(dm2.OperatorID AS NVARCHAR(50))
							FROM #DmPBThayDoi dm2
							WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								  dm2.LoaiThayDoi = 8 AND 
								  dm2.Operator_Type = 1
							FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OperatorList
				FROM #DmPBThayDoi dm1
				WHERE dm1.LoaiThayDoi = 8 AND dm1.Operator_Type = 1
				GROUP BY dm1.HopDongChiTietID
			) pb_operator ON dm.HopDongChiTietID = pb_operator.HopDongChiTietID
		WHERE dm.LoaiThayDoi = 8 AND dm.Operator_Type = 1

	END

	--===============9: ADS_Operating_Result thay đổi TT hoặc [ADS_Operating_Result_Map_Order] thay đổi result_id => thay đổi thành tiền mua của order 
	INSERT INTO #DmPBThayDoi
		(    HopDongID
			,HopDongChiTietID 	
			,OrderID
			,ResultID
			,IsActive_hdct 
			,IsActive_Order 
			,LoaiThayDoi
			,LoaiXuLy)
	SELECT	DISTINCT
			R.HopDongFK,
			R.Contract_Detail_Id,
			R.Operating_Order_Id,
			R.Id,
			1,
			1,
			9,
			2
	FROM (
			SELECT  R.id, R.IsDeleted, R.Total_Money_VND, R.Operating_Order_Id, OD.Contract_Detail_Id, hdct.HopDongFK
			FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result R
			INNER JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Order OD ON OD.ID = R.Operating_Order_Id
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE CONVERT(date,R.LastModificationTime) = @NgayCheckThayDoi
					--AND OD.Contract_Detail_Id NOT IN (SELECT HopDongChiTietID
					--								  FROM #DmPBThayDoi )
					AND hdct.DeletedStatus = 0 
					AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong <> 3
					AND OD.IsDeleted = 0
			) R
	OUTER APPLY 
			(
			SELECT TOP 1 L.IsDeleted, L.Total_Money_VND, L.Operating_Order_Id
			FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Log L
			WHERE CONVERT(date,L.LastModificationTime) < @NgayCheckThayDoi
					AND L.ADS_Operating_Result_Id = R.Id
			ORDER BY L.LastModificationTime DESC 
			) L
	WHERE @SoHopDong IS NULL 
			AND ( R.IsDeleted = 1  OR 
				ISNULL(R.Total_Money_VND, 0) <> ISNULL(L.Total_Money_VND, 0) OR 
				ISNULL(R.Operating_Order_Id, 0) <> ISNULL(L.Operating_Order_Id, 0)
				)
			AND L.IsDeleted = 0

	DELETE dm
	FROM #DmPBThayDoi dm
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = dm.HopDongID
	WHERE hd.NgayDanhSoHopDong < @NgayDanhSoGioiHan AND 
		  @NgayDanhSoGioiHan IS NOT NULL


	UPDATE dm
	SET Lydo = N'order ' + pb_Order.OrderList + N' thay đổi thành tiền mua bởi phát sinh result hủy/ chuyển order/ thay đổi thành tiền'
	FROM #DmPBThayDoi dm
	JOIN (	SELECT dm1.HopDongChiTietID,
					STUFF((
						SELECT DISTINCT ',' + CAST(dm2.OrderID AS NVARCHAR(50))
						FROM #DmPBThayDoi dm2
						WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID AND 
								dm2.LoaiThayDoi = 9 
						FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS OrderList
			FROM #DmPBThayDoi dm1
			WHERE dm1.LoaiThayDoi = 9
			GROUP BY dm1.HopDongChiTietID
		) pb_Order ON dm.HopDongChiTietID = pb_Order.HopDongChiTietID
	WHERE dm.LoaiThayDoi = 9

	--=================================================== Xác định thực chạy cần tính lại của mỗi phân bổ =====================================
	-- chú ý: dữ liệu vận hành phải đảm bảo lastmodifiedTime < cast(getdate as date)
	BEGIN
		CREATE TABLE #DmTinhLai_TheoOrder 
		(		 ID INT 
				,HopDongID INT				
				,HopDongChiTietID INT	
				,Order_Id INT
				,DonViTinh NVARCHAR(100)
				,DmNhanHang INT
				,DmWebsiteID INT
				,ChietKhau FLOAT

				,ThanhTienChay FLOAT
				,SoLuongChay FLOAT
				,DonGiaChay FLOAT
				,DuToanMuaSauCK FLOAT 
				,ThanhTienMua FLOAT

				,NganSachOrder FLOAT
				,ThanhTien_HDCT FLOAT
				
				,ThanhTien_GhiNhan_Order FLOAT

				,ThanhTien_GhiNhan FLOAT
				,SoLuong_GhiNhan FLOAT
				,ThanhTienLai FLOAT

				,Type INT
		)

		INSERT INTO #DmTinhLai_TheoOrder 
		(		 ID
				,HopDongID 
				,HopDongChiTietID 
				,Order_Id 
				,DonViTinh 
				,DmNhanHang
				,DmWebsiteID
				,ChietKhau 

				,ThanhTienChay
				,SoLuongChay 
				,DuToanMuaSauCK  
				,ThanhTienMua

				,NganSachOrder 
				,ThanhTien_HDCT

				,Type
		)
		SELECT  TC.ID,
				HopDongID = hdct.HopDongFK, 
				HopDongChiTietID = OD.Contract_Detail_Id,
				Order_Id = TC.Operating_Order_Id,
				DonViTinh = IIF(OD.UNITS = '', N'GÓI', OD.UNITS), 
				DmNhanHang = OD.Brand_id,
				DmWebsiteID = OD.DmWebsiteREF,
				hdct.ChietKhau,
					
				ThanhTienChay = ISNULL(TC.Sell_Money_VND,0),
				SoLuongChay = IIF(ISNULL(TC.Result,0) = 0, 1, TC.Result) ,
				DuToanMuaSauCK = 0,
				ThanhTienMua = ISNULL(RS.Total_Money_VND, 0),

				NganSachOrder = OD.Money_Turnover ,
				ThanhTien_HDCT = IIF(hdct.KhuyenMai = 100, hdct.SoLuong*hdct.DonGia, hdct.ThanhTien),

				Type = 1
		FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Map_Order TC
		INNER JOIN ABM_Data_ThucChay.DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = OD.Contract_Detail_Id
		LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Result RS ON RS.Id = TC.operating_Result_Id
		INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID
					FROM #DmPBThayDoi dm 
					WHERE dm.IsActive_hdct = 1 AND dm.LoaiXuLy = 2) dm ON dm.HopDongChiTietID = hdct.HopDongChiTietID
		WHERE   TC.IsDeleted = 0
				AND ISNULL(TC.Sell_Money_VND,0) <> 0
				AND CONVERT(DATE,TC.LastModificationTime) < CAST(GETDATE() AS DATE)
				-- không xử lý treo ghi nhận mới trong luồng thay đổi
				AND NOT (CONVERT(DATE,TC.LastModificationTime) = @NgayGhiNhan AND   
						 (TC.IsCaculatedActual = 0 OR
						  TC.ID IN (SELECT ID FROM #dmIDtinhmoi WHERE type = 1)))
				AND ISNULL(OD.IsDeleted,0) =0

		UNION ALL
		SELECT  TC.Id,
				HopDongID = hdct.HopDongFK, 
				HopDongChiTietID = OD.Contract_Detail_Id,
				Order_Id = TC.Operating_Order_Id,	
				DonViTinh = IIF(OD.UNITS = '', N'GÓI', OD.UNITS), 
				DmNhanHang = OD.Brand_id,
				DmWebsiteID = OD.DmWebsiteREF,
				hdct.ChietKhau,

				ThanhTienChay = ISNULL(TC.TotalMoney,0),
				SoLuongChay = IIF(ISNULL(TC.Quantity,0) = 0, 1, TC.Quantity) ,
				DuToanMuaSauCK = 0,
				ThanhTienMua = RS.ThanhTienMua,

				NganSachOrder = OD.Money_Turnover ,
				ThanhTien_HDCT = IIF(hdct.KhuyenMai = 100, hdct.SoLuong*hdct.DonGia, hdct.ThanhTien),

				Type =2
		FROM ABM_Data_ThucChay.dbo.[ADS_Operating_Result_Quantity] TC
		INNER JOIN ABM_Data_ThucChay.DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
		INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID
					FROM #DmPBThayDoi dm 
					WHERE dm.IsActive_hdct = 1 AND dm.LoaiXuLy = 2) dm ON dm.HopDongChiTietID = hdct.HopDongChiTietID
		OUTER APPLY (	SELECT ThanhTienMua = SUM(ISNULL(RS.Total_Money_VND, 0))
						FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result RS 
						WHERE RS.Operating_Order_Id = TC.Operating_Order_Id AND 
								RS.Date_result BETWEEN TC.fromdate AND TC.toDate AND 
								RS.IsDeleted = 0) RS
		WHERE   TC.Status = 2 
				AND isnull(TC.IsDeleted,0) = 0
				AND ISNULL(TC.TotalMoney,0) <> 0 
				AND CONVERT(DATE,TC.LastModificationTime) < CAST(GETDATE() AS DATE)
				-- không xử lý treo ghi nhận mới trong luồng thay đổi
				AND NOT (CONVERT(DATE,TC.LastModificationTime) = @NgayGhiNhan AND   
						 (TC.IsCalc_Result_Quantity = 0 OR
						  TC.ID IN (SELECT ID FROM #dmIDtinhmoi WHERE type = 2)))
				
			


		UPDATE dm
		SET dm.DonGiaChay = dm.ThanhTienChay/dm.SoLuongChay
		FROM #DmTinhLai_TheoOrder dm

	END

	--=================================================  Xác định thực chạy được ghi nhận và lệch treo hạ
	BEGIN
		-- chặn vượt ngân sách
		;WITH CTE_Base AS (
				SELECT  ID,
						TongThucChayTruocDo_Order =  COALESCE(	SUM(ThanhTienChay) OVER (
																PARTITION BY Order_Id  
																ORDER BY ID, Type  
																ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
																), 0) ,
						TongThucChayDenHT_Order =    COALESCE(	SUM(ThanhTienChay) OVER (
																PARTITION BY Order_Id
																ORDER BY ID, Type 
																ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
																), 0)
				FROM #DmTinhLai_TheoOrder 
				)

		UPDATE temp
		SET ThanhTien_GhiNhan_Order =   CASE	WHEN sl.TongThucChayDenHT_Order <= temp.NganSachOrder
												THEN temp.ThanhTienChay
												WHEN sl.TongThucChayDenHT_Order > temp.NganSachOrder AND 
													 sl.TongThucChayTruocDo_Order <= temp.NganSachOrder
												THEN temp.NganSachOrder - sl.TongThucChayTruocDo_Order
												WHEN sl.TongThucChayDenHT_Order > temp.NganSachOrder AND 
													 sl.TongThucChayTruocDo_Order > temp.NganSachOrder
												THEN 0
										END
		FROM #DmTinhLai_TheoOrder temp
		INNER JOIN CTE_Base sl ON sl.ID = temp.ID

		-- chặn vượt phân bổ
		;WITH CTE_Base_2 AS (
				SELECT  ID,
						TongThucChayTruocDo_HDCT =  COALESCE(	SUM(ThanhTien_GhiNhan_Order) OVER (
																PARTITION BY HopDongChiTietID  
																ORDER BY Order_Id, ID, Type  
																ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
																), 0) ,
						TongThucChayDenHT_HDCT =    COALESCE(	SUM(ThanhTien_GhiNhan_Order) OVER (
																PARTITION BY HopDongChiTietID  
																ORDER BY Order_Id, ID, Type 
																ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
																), 0)
				FROM #DmTinhLai_TheoOrder 
				)

		UPDATE temp
		SET ThanhTien_GhiNhan   =       CASE    WHEN sl.TongThucChayDenHT_HDCT <= temp.ThanhTien_HDCT
												THEN temp.ThanhTien_GhiNhan_Order
												WHEN sl.TongThucChayDenHT_HDCT > temp.ThanhTien_HDCT AND 
													 sl.TongThucChayTruocDo_HDCT <= temp.ThanhTien_HDCT
												THEN temp.ThanhTien_HDCT - sl.TongThucChayTruocDo_HDCT
												WHEN sl.TongThucChayDenHT_HDCT > temp.ThanhTien_HDCT AND 
													 sl.TongThucChayTruocDo_HDCT > temp.ThanhTien_HDCT
												THEN 0
										END
		FROM #DmTinhLai_TheoOrder temp
		INNER JOIN CTE_Base_2 sl ON sl.ID = temp.ID

		UPDATE dm
		SET dm.SoLuong_GhiNhan = ThanhTien_GhiNhan / DonGiaChay
		FROM #DmTinhLai_TheoOrder dm

		UPDATE dm
		SET dm.ThanhTienLai = IIF(ChietKhau = 100, ThanhTienChay - ThanhTienMua, ThanhTien_GhiNhan - ThanhTienMua)
		FROM #DmTinhLai_TheoOrder dm
	END

	--===================================================== Đối trừ và insert Thucchaydatinh==================================
	INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
			([ThucChayDaTinhID]
			,[HopDongID]
			,[SoHopDong]
			,[DmMaHopDongREF]
			,[TenMaHopDong]
			,[NgayDanhSoHopDong]
			,[NgayKyHopDong]
			,[NhanHopDong]
			,[NgayNhanBanFax]
			,[NgayNhanHopDongBanCung]
			,[NgayChuyenHopDongChoKeToan]
			,[So]
			,[Thang]
			,[Nam]
			,[GiaTriHopDong]
			,[CongNo]
			,[HopDongChiTietREF]
			,[DangSuDung]
			,[IsGiayPhep]
			,[TrangThaiHopDong]
			,[IsBanCung]
			,[DmPhongBanREF]
			,[TenPhongBan]
			,[DmBoPhanREF]
			,[TenBoPhan]
			,[DmNhomLamViecREF]
			,[TenNhomLamViec]
			,[DmDiaDiemLamViecREF]
			,[TenDiaDiemLamViec]
			,[SysNhanVienREF]
			,[TenDangNhap]
			,[TenNhanVien]
			,[TenKhachHang]
			,[NhanHang]
			,[DmNhomNganhREF]
			,[TenNhomNganh]
			,[DmHinhThucQuangCao]
			,[TenHinhThucQuangCao]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[DmNhomWebsiteREF]
			,[TenNhomWebsite]
			,[DmChuyenMucREF]
			,[TenChuyenMuc]
			,[DmLoaiBannerREF]
			,[TenLoaiBanner]
			,[DmViTriREF]
			,[TenViTri]
			,[DotChayHopDong]
			,[SoLuongDotChayHD]
			,[DotChayBooking]
			,[SoLuongDotChayBooking]
			,[SoLuong]
			,[DonViTinh]
			,[DonGia]
			,[DonGiaTheoDonVi]
			,[ChietKhau]
			,[GiamGia]
			,[ThanhTien]
			,[TiLeTuVan]
			,[ChiPhiTuVan]
			,[IsKhuyenMai]
			,[KhuyenMai]
			,[DmBannerREF]
			,[DmChienDichREF]
			,[DmWebsiteREF]
			,[TenWebsite]
			,[TongViewThucChay] 
			,[TongClickThucChay] 
			,[TongSoBaiViet] 
			,[SoLuongThucChay]
			,[GiaTriThayDoi]
			,[ThanhTienThucChayTruocTrietKhau]
			,[GiaTriTrietKhauThucChay]
			,[ThanhTienSauTrietKhauThucChay]
			,[GiaTriHoaHongThucChay]
			,[ThanhTienThucThu]
			,[ThanhTienKM]
			,[SoLuongThucChayKM]
			,[SoLuongThucChayLechTreoHa]
			,[ThanhTienLechTreoHa]
			,[CreatedAt]
			,[LastModifiedAt]
			,[IsPheDuyet]
			,[PheDuyetBy]
			,[PheDuyetAt]
			,[SoLuongThayDoi]
			,[SoLuongKMThayDoi]
			,[GiaTriKMThayDoi]
			,[GhiChu]
			,[NgayThucHien])
	SELECT		 NEWID()
				,tcdt.HopDongID
				,[SoHopDong]
				,[DmMaHopDongREF]
				,[TenMaHopDong]
				,[NgayDanhSoHopDong]
				,[NgayKyHopDong]
				,[NhanHopDong]
				,[NgayNhanBanFax]
				,[NgayNhanHopDongBanCung]
				,[NgayChuyenHopDongChoKeToan]
				,[So]
				,[Thang]
				,[Nam]
				,[GiaTriHopDong]
				,[CongNo]
				,[HopDongChiTietREF]
				,[DangSuDung]
				,[IsGiayPhep]
				,[TrangThaiHopDong]
				,[IsBanCung]
				,[DmPhongBanREF]
				,[TenPhongBan]
				,[DmBoPhanREF]
				,[TenBoPhan]
				,[DmNhomLamViecREF]
				,[TenNhomLamViec]
				,[DmDiaDiemLamViecREF]
				,[TenDiaDiemLamViec]
				,[SysNhanVienREF]
				,[TenDangNhap]
				,[TenNhanVien]
				,[TenKhachHang]
				,[NhanHang]
				,[DmNhomNganhREF]
				,[TenNhomNganh]
				,[DmHinhThucQuangCao]
				,[TenHinhThucQuangCao]
				,[DmSanPhamREF]
				,[TenSanPham]
				,[DmNhomWebsiteREF]
				,[TenNhomWebsite]
				,[DmChuyenMucREF]
				,[TenChuyenMuc]
				,[DmLoaiBannerREF]
				,[TenLoaiBanner]
				,[DmViTriREF]
				,[TenViTri]
				,N'Tính thay đổi GGFB' 
				,[SoLuongDotChayHD] = 0
				,[DotChayBooking] = 0
				,[SoLuongDotChayBooking] = 0
				,[SoLuong]
				,[DonViTinh]
				,[DonGia]
				,[DonGiaTheoDonVi]
				,[ChietKhau]
				,[GiamGia]
				,[ThanhTien]
				,[TiLeTuVan]
				,[ChiPhiTuVan]
				,[IsKhuyenMai]
				,[KhuyenMai]
				,[DmBannerREF]
				,[DmChienDichREF]
				,[DmWebsiteREF]
				,[TenWebsite]
				,[TongViewThucChay] = 0
				,[TongClickThucChay] = 0
				,[TongSoBaiViet] = 0
				,[SoLuongThucChay] = 0
				,SUM([GiaTriThayDoi]) 
				,SUM([ThanhTienThucChayTruocTrietKhau]) 
				,SUM([GiaTriTrietKhauThucChay])
				,[ThanhTienSauTrietKhauThucChay] = 0
				,SUM([GiaTriHoaHongThucChay])
				,SUM([ThanhTienThucThu])
				,[ThanhTienKM] = 0
				,[SoLuongThucChayKM] = 0
				,[SoLuongThucChayLechTreoHa] = ROUND(SUM([SoLuongThucChayLechTreoHa]), 0)
				,SUM([ThanhTienLechTreoHa])
				,GETDATE() AS [CreatedAt]
				,GETDATE() AS [LastModifiedAt]
				,0 AS [IsPheDuyet]
				,'' AS [PheDuyetBy]
				,'' AS [PheDuyetAt]
				,[SoLuongThayDoi] = ROUND(SUM([SoLuongThayDoi]), 0)
				,[SoLuongKMThayDoi] = ROUND(SUM([SoLuongKMThayDoi]), 0)
				,SUM([GiaTriKMThayDoi]) 
				, N'Tính thay đổi: SP tối ưu [dbo].[ThucChay_GGFB_GhiNhanThayDoi] do ' + dm.LyDo
				, @NgayGhiNhan
	FROM (	
			SELECT   tcdt.HopDongID
					,tcdt.[SoHopDong]
					,tcdt.[DmMaHopDongREF]
					,tcdt.[TenMaHopDong]
					,tcdt.[NgayDanhSoHopDong]
					,tcdt.[NgayKyHopDong]
					,tcdt.[NhanHopDong]
					,tcdt.[NgayNhanBanFax]
					,tcdt.[NgayNhanHopDongBanCung]
					,tcdt.[NgayChuyenHopDongChoKeToan]
					,tcdt.[So]
					,tcdt.[Thang]
					,tcdt.[Nam]
					,tcdt.[GiaTriHopDong]
					,tcdt.[CongNo]
					,tcdt.[HopDongChiTietREF]
					,tcdt.[DangSuDung]
					,tcdt.[IsGiayPhep]
					,tcdt.[TrangThaiHopDong]
					,tcdt.[IsBanCung]
					,tcdt.[DmPhongBanREF]
					,tcdt.[TenPhongBan]
					,tcdt.[DmBoPhanREF]
					,tcdt.[TenBoPhan]
					,tcdt.[DmNhomLamViecREF]
					,tcdt.[TenNhomLamViec]
					,tcdt.[DmDiaDiemLamViecREF]
					,tcdt.[TenDiaDiemLamViec]
					,tcdt.[SysNhanVienREF]
					,tcdt.[TenDangNhap]
					,tcdt.[TenNhanVien]
					,tcdt.[TenKhachHang]
					,tcdt.[NhanHang]
					,tcdt.[DmNhomNganhREF]
					,tcdt.[TenNhomNganh]
					,tcdt.DmHinhThucQuangCao
					,tcdt.TenHinhThucQuangCao
					,tcdt.[DmSanPhamREF]
					,tcdt.TenSanPham
					,tcdt.DmNhomWebsiteREF
					,tcdt.TenNhomWebsite
					,[tcdt].[DmChuyenMucREF]
					,tcdt.TenChuyenMuc
					,tcdt.DmLoaiBannerREF
					,tcdt.[TenLoaiBanner]
					,tcdt.[DmViTriREF]
					,tcdt.[TenViTri]
					,tcdt.[SoLuong]
					,tcdt.[DonViTinh]
					,tcdt.[DonGia]
					,tcdt.[DonGiaTheoDonVi]
					,tcdt.[ChietKhau]
					,tcdt.[GiamGia]
					,tcdt.[ThanhTien]
					,tcdt.[TiLeTuVan]
					,tcdt.[ChiPhiTuVan]
					,tcdt.[IsKhuyenMai]
					,tcdt.[KhuyenMai]
					,tcdt.[DmBannerREF]
					,tcdt.[DmChienDichREF]
					,tcdt.[DmWebsiteREF]
					,tcdt.[TenWebsite]
					,-([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
					,0 AS [ThanhTienThucChayTruocTrietKhau]
					,-([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
					,-(tcdt.[SoLuongThucChay] + tcdt.[SoLuongThayDoi]) AS [SoLuongThayDoi]
					,-(tcdt.[SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
					,-(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
					,-(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay
					,0 AS ThanhTienThucThu
					,-(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
					,-(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			FROM ABM_Data_ThucChay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID
						FROM #DmPBThayDoi dm) dm ON dm.HopDongChiTietID = tcdt.HopDongChiTietREF
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien <= @NgayGhiNhan 
						AND (tcdt.DmSanPhamREF in (306,423,5160,5188,772)  OR tcdt.DmViTriREF in (100093,100478,100774))
						AND NOT (tcdt.DmHinhThucQuangCao IN(13) OR tcdt.DmLoaiBannerREF IN (18))
						AND tcdt.DmSanPhamREF <> 585
			UNION ALL
			SELECT	HopDongID = hd.HopDongID,
					SoHopDong = hd.SoHopDong,
					DmMaHopDongREF = hd.DmMaHopDongREF,
					TenMaHopDong = hd.TenMaHopDong,
					NgayDanhSoHopDong = hd.NgayDanhSoHopDong,
					NgayKyHopDong = hd.NgayKyHopDong,
					NhanHopDong = hd.NhanHopDong,
					NgayNhanBanFax = hd.NgayNhanBanFax,
					NgayNhanHopDongBanCung = hd.NgayNhanHopDongBanCung,
					NgayChuyenHopDongChoKeToan = hd.NgayChuyenHopDongChoKeToan,
					So = hd.So,
					Thang = hd.Thang,
					Nam = hd.Nam,
					GiaTriHopDong = hd.GiaTriHopDong,
					CongNo = hd.CongNo,
					HopDongChiTietREF = hdct.HopDongChiTietID,
					DangSuDung = hd.DangSuDung,
					IsGiayPhep = hd.IsGiayPhep,
					TrangThaiHopDong = hd.TrangThaiHopDong,
					IsBanCung = hd.IsBanCung,
					DmPhongBanREF = ISNULL(hd.DmPhongBanREF,0),		
					TenPhongBan = ISNULL(HD.TenPhongBan,''),					
					DmBoPhanREF = ISNULL(HD.DmBoPhanREF,0),				
					TenBoPhan = ISNULL(HD.TenBoPhan,'')	,			
					DmNhomLamViecREF = ISNULL(HD.DmNhomLamViecREF,0),				
					TenNhomLamViec = ISNULL(HD.TenNhom,''),				
					DmDiaDiemLamViecREF = HD.DmDiaDiemLamViecREF, 				
					TenDiaDiemLamViec = ISNULL(HD.TenDiaDiemLamViec,''),				
					SysNhanVienREF = HD.SysNhanVienREF,				
					TenDangNhap = HD.TenDangNhap,				
					TenNhanVien = HD.TenNhanVien,				
					TenKhachHang = HD.TenKhachHang,		
					NhanHang = dm.DmNhanHang,
					DmNhomNganhREF = HDCT.DmNhomNganhREF,				
					TenNhomNganh = ISNULL(HDCT.TenNhomNganh,''),				
					DmHinhThucQuangCao = HDCT.DmLoaiREF,				
					TenHinhThucQuangCao = HDCT.TenLoai,				
					DmSanPhamREF = HDCT.DmSanPhamREF,				
					TenSanPham = HDCT.TenSanPham,				
					DmNhomWebsiteREF = HDCT.DmNhomWebsiteREF,				
					TenNhomWebsite = HDCT.TenNhomWebsite,				
					DmChuyenMucREF= HDCT.DmChuyenMucREF,			
					TenChuyenMuc = HDCT.TenChuyenMuc,			
					DmLoaiBannerREF= HDCT.DmLoaiBannerREF,				
					TenLoaiBanner = HDCT.TenLoaiBanner,					
					DmViTriREF = HDCT.DmViTriREF,						
					TenViTri  = HDCT.TenViTri,	
					SoLuong = hdct.SoLuong,
					DonViTinh = [dbo].[FormatDonViTinh_ThanhTien_GGFB](dm.DonViTinh),
					DonGia = hdct.DonGia,
					DonGiaTheoDonVi = dm.DonGiaChay,
					ChietKhau = hdct.ChietKhau,
					GiamGia  = HDCT.GiamGia,					
					ThanhTien  = HDCT.ThanhTien,						
					TiLeTuVan   = HDCT.TiLeTuVan,                
					ChiPhiTuVan = HDCT.ChiPhiTuVan,                       
					IsKhuyenMai = HDCT.IsKhuyenMai,                 
					KhuyenMai   = HDCT.KhuyenMai,                     
					DmBannerREF = HDCT.DmBannerREF ,
					DmChienDichREF = dm.Order_Id,
					DmWebsiteREF = w.DmWebsiteReportingdbID,   
					TenWebsite = ISNULL(w.WebsiteLink, N''),  
					GiaTriThayDoi = IIF(hdct.ChietKhau = 100, 0, dm.ThanhTien_GhiNhan),
					ThanhTienThucChayTruocTrietKhau = 0,
					GiaTriTrietKhauThucChay = IIF(hdct.ChietKhau = 100, 0, ThanhTien_GhiNhan*hdct.ChietKhau/(100-hdct.ChietKhau)),
					SoLuongThayDoi = IIF(hdct.ChietKhau = 100, 0, dm.SoLuong_GhiNhan),
					SoLuongKMThayDoi = IIF(hdct.ChietKhau = 100, SoLuong_GhiNhan, 0),
					GiaTriKMThayDoi = IIF(hdct.ChietKhau = 100, ThanhTien_GhiNhan, 0),
					GiaTriHoaHongThucChay = IIF(hdct.ChietKhau = 100, 0, ThanhTien_GhiNhan*hdct.TiLeTuVan/100),
					ThanhTienThucThu = 0,
					SoLuongThucChayLechTreoHa = SoLuongChay - SoLuong_GhiNhan,
					ThanhTienLechTreoHa = IIF(hdct.ChietKhau = 100, ThanhTienChay - ThanhTien_GhiNhan, (ThanhTienChay - ThanhTien_GhiNhan)/(1-hdct.ChietKhau/100))
		FROM #DmTinhLai_TheoOrder dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
		INNER JOIN ABM_Data_ThucChay.dbo.hopDong hd ON hd.HopDongID = hdct.HopDongFK
		OUTER APPLY (SELECT TOP 1 DmWebsiteReportingdbID, WebsiteLink
						FROM ABM_Data_ThucChay.dbo.WebsiteMapping_HDCN_Reporting w 
						WHERE w.DmWebsiteID = ISNULL(dm.DmWebsiteID, 265) ) w
	) tcdt
	INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID, 
								LyDo = N'phân bổ ' + CAST(dm.HopDongChiTietID AS NVARCHAR(50)) + N' có: ' + pb_LyDo.DsLyDo
				FROM #DmPBThayDoi dm
				JOIN (	SELECT dm1.HopDongChiTietID,
								STUFF((
									SELECT DISTINCT ';  ' + dm2.LyDo
									FROM #DmPBThayDoi dm2
									WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS DsLyDo
						FROM #DmPBThayDoi dm1
						GROUP BY dm1.HopDongChiTietID
					) pb_LyDo ON dm.HopDongChiTietID = pb_LyDo.HopDongChiTietID
				) dm ON dm.HopDongChiTietID = tcdt.HopDongChiTietREF
	GROUP BY		 tcdt.[HopDongID]
					,[SoHopDong]
					,[DmMaHopDongREF]
					,[TenMaHopDong]
					,[NgayDanhSoHopDong]
					,[NgayKyHopDong]
					,[NhanHopDong]
					,[NgayNhanBanFax]
					,[NgayNhanHopDongBanCung]
					,[NgayChuyenHopDongChoKeToan]
					,[So]
					,[Thang]
					,[Nam]
					,[GiaTriHopDong]
					,[CongNo]
					,[HopDongChiTietREF]
					,[DangSuDung]
					,[IsGiayPhep]
					,[TrangThaiHopDong]
					,[IsBanCung]
					,[DmPhongBanREF]
					,[TenPhongBan]
					,[DmBoPhanREF]
					,[TenBoPhan]
					,[DmNhomLamViecREF]
					,[TenNhomLamViec]
					,[DmDiaDiemLamViecREF]
					,[TenDiaDiemLamViec]
					,[SysNhanVienREF]
					,[TenDangNhap]
					,[TenNhanVien]
					,[TenKhachHang]
					,[NhanHang]
					,[DmNhomNganhREF]
					,[TenNhomNganh]
					,[DmHinhThucQuangCao]
					,[TenHinhThucQuangCao]
					,[DmSanPhamREF]
					,[TenSanPham]
					,[DmNhomWebsiteREF]
					,[TenNhomWebsite]
					,[DmChuyenMucREF]
					,[TenChuyenMuc]
					,[DmLoaiBannerREF]
					,[TenLoaiBanner]
					,[DmViTriREF]
					,[TenViTri]
					,[SoLuong]
					,[DonViTinh]
					,[DonGia]
					,[DonGiaTheoDonVi]
					,[ChietKhau]
					,[GiamGia]
					,[ThanhTien]
					,[TiLeTuVan]
					,[ChiPhiTuVan]
					,[IsKhuyenMai]
					,[KhuyenMai]
					,[DmBannerREF]
					,[DmChienDichREF]
					,[DmWebsiteREF]
					,[TenWebsite]
					,dm.LyDo
	HAVING SUM(tcdt.[GiaTriThayDoi]) <> 0
			OR SUM(tcdt.[GiaTriKMThayDoi]) <> 0
			OR SUM(SoLuongThucChayLechTreoHa) <> 0
			OR SUM(ThanhTienLechTreoHa) <> 0
			OR SUM(tcdt.SoLuongThayDoi) <> 0 
			OR SUM(tcdt.SoLuongKMThayDoi) <> 0


	--===================================================== Đối trừ và insert Thucchaydatinh_muangoai ==================================
	INSERT INTO ABM_Data_ThucChay.[dbo].ThucChayDaTinh_MuaNgoai
	(
	    HopDongREF,
	    SoHopDong,
	    DmMaHopDongREF,
	    NgayDanhSoHopDong,
	    TrangThaiHopDong,
	    DmNhanVienREF,
	    TenDangNhap,
	    DmPhongBanREF,
	    DmBoPhanREF,
	    DmNhomLamViecREF,
	    DmDiaDiemLamViecREF,
	    DmKhachHangREF,
	    HopDongChiTietREF,
	    LstDmNhanHangREF,
	    LstDmNhomNganhREF,
	    DmHinhThucQuangCaoREF,
	    DmSanPhamREF,
	    DmChuyenMucREF,
	    DmLoaiBannerREF,
	    DmViTriREF,
	    SoLuong,
	    DonViTinhREF,
	    DonGia,
	    ChietKhau,
	    ThanhTien,
	    IsKhuyenMai,
	    KhuyenMai,
	    ThucChayMuaNgoaiChiTietREF,
	    TongTienDuToanMuaSauCK,
	    TongTienDuToanLaiMuaSauCK,
	    ChietKhauMua,
	    DmBannerREF,
	    DmChienDichREF,
	    DmWebsiteREF,
	    TenWebsite,
	    NgayThucHien,
	    NgayBatDau,
	    NgayKetThuc,
	    DonViTinhThucChay,
	    DonGiaTheoDonViTinhTC,
	    TongViewClickThucChay,
	    TongSoBaiVietChiPhiThucChay,
	    SoLuongThucChay,
	    TongThanhTienThucChayBanSauCK,
	    TongThanhTienThucChayMuaSauCK,
	    ThanhTienLaiThucChaySauCK,
	    ThanhTienLaiThucChayKM,
	    SoLuongThucChayKM,
	    SoLuongThucChayLechTreoHa,
	    ThanhTienLechTreoHa,
	    GiaTriThayDoiLaiSauCK,
	    SoLuongThayDoi,
	    SoLuongKMThayDoi,
	    GiaTriKMLaiThayDoi,
	    GhiChu,
	    CreatedAt,
	    LastModifiedAt
	)
	SELECT		    HopDongREF,
					SoHopDong,
					DmMaHopDongREF,
					NgayDanhSoHopDong,
					TrangThaiHopDong,
					DmNhanVienREF,
					TenDangNhap,
					DmPhongBanREF,
					DmBoPhanREF,
					DmNhomLamViecREF,
					DmDiaDiemLamViecREF,
					DmKhachHangREF,
					HopDongChiTietREF,
					LstDmNhanHangREF,
					LstDmNhomNganhREF,
					DmHinhThucQuangCaoREF,
					DmSanPhamREF,
					DmChuyenMucREF,
					DmLoaiBannerREF,
					DmViTriREF,
					SoLuong,
					DonViTinhREF,
					DonGia,
					ChietKhau,
					ThanhTien,
					IsKhuyenMai,
					KhuyenMai,
					ThucChayMuaNgoaiChiTietREF = 0,
					TongTienDuToanMuaSauCK = 0,
					SUM(TongTienDuToanLaiMuaSauCK ),
					ChietKhauMua = 0,
					DmBannerREF,
					DmChienDichREF,
					DmWebsiteREF,
					TenWebsite,
					@NgayGhiNhan,
					NgayBatDau = NULL,
					NgayKetThuc = NULL,
					DonViTinhThucChay,
					DonGiaTheoDonViTinhTC,
					TongViewClickThucChay = 0,
					TongSoBaiVietChiPhiThucChay = 0,
					SoLuongThucChay = 0,
					SUM(TongThanhTienThucChayBanSauCK),
					SUM(TongThanhTienThucChayMuaSauCK),
					ThanhTienLaiThucChaySauCK = 0,
					ThanhTienLaiThucChayKM = 0,
					SoLuongThucChayKM = 0,
					SoLuongThucChayLechTreoHa = 0,
					ThanhTienLechTreoHa = 0,
					SUM(GiaTriThayDoiLaiSauCK),
					SoLuongThayDoi = ROUND(SUM(SoLuongThayDoi), 0),
					SoLuongKMThayDoi = ROUND(SUM(SoLuongKMThayDoi), 0),
					SUM(GiaTriKMLaiThayDoi),
					GhiChu = N'Ghi nhận thay đổi: SP tối ưu [dbo].[ThucChay_GGFB_GhiNhanThayDoi] do ' + dm.LyDo,
					CreatedAt = GETDATE(),
					LastModifiedAt = GETDATE()
	FROM  (
			SELECT  	    HopDongREF = hdct.HopDongFK
						   ,[SoHopDong] = HD.[SoHopDong]  
						   ,[DmMaHopDongREF]  = HD.[DmMaHopDongREF] 
						   ,[NgayDanhSoHopDong] = HD.[NgayDanhSoHopDong]    
						   ,[TrangThaiHopDong] = hd.TrangThaiHopDong  
						   ,[DmNhanVienREF] = HD.SysNhanVienREF     
						   ,[TenDangNhap] = HD.[TenDangNhap]    
						   ,[DmPhongBanREF] = HD.[DmPhongBanREF]    
						   ,[DmBoPhanREF] = HD.[DmBoPhanREF]   
						   ,[DmNhomLamViecREF] = HD.[DmNhomLamViecREF]      
						   ,[DmDiaDiemLamViecREF] = HD.[DmDiaDiemLamViecREF]    
						   ,[DmKhachHangREF]  = HD.[DmKhachHangREF]    
						   ,[HopDongChiTietREF] = hdct.HopDongChiTietID
						   ,LstDmNhanHangREF = dm.DmNhanHang
						   ,[LstDmNhomNganhREF] = HDCT.DmNhomNganhREF   
						   ,[DmHinhThucQuangCaoREF] = HDCT.DmLoaiREF   
						   ,[DmSanPhamREF] = HDCT.DmSanPhamREF   
						   ,[DmChuyenMucREF] =  HDCT.[DmChuyenMucREF]   
						   ,[DmLoaiBannerREF] =  HDCT.[DmLoaiBannerREF]    
						   ,[DmViTriREF]  =  HDCT.[DmViTriREF]   
						   ,[SoLuong] =  HDCT.[SoLuong]     
						   ,[DonViTinhREF]  =  HDCT.[DonViTinhREF]     
						   ,[DonGia]  =  HDCT.[DonGia]     
						   ,[ChietKhau]   =  HDCT.[ChietKhau]  
						   ,[ThanhTien]  =  HDCT.[ThanhTien]   
						   ,[IsKhuyenMai]  =  HDCT.[IsKhuyenMai]    
						   ,[KhuyenMai]  =  HDCT.[KhuyenMai]    
						   ,TongTienDuToanLaiMuaSauCK = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, 0, HDCT.ThanhTien )  
						   ,DmBannerREF = hdct.DmBannerREF
						   ,DmChienDichREF = dm.Order_Id
						   ,DmWebsiteREF = w.DmWebsiteReportingdbID  
						   ,TenWebsite = ISNULL(w.WebsiteLink, N'')
						   ,DonViTinhThucChay = [dbo].[FormatDonViTinh_ThanhTien_GGFB](dm.DonViTinh)
						   ,DonGiaTheoDonViTinhTC = dm.DonGiaChay
						   ,[TongThanhTienThucChayBanSauCK]  = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 , 0, dm.ThanhTien_GhiNhan)
						   ,[TongThanhTienThucChayMuaSauCK] = dm.ThanhTienMua
						   ,[GiaTriThayDoiLaiSauCK] = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 , 0, dm.ThanhTienLai)
						   ,[SoLuongThayDoi] = IIF (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 ,--OR dm.ThanhTienLai <= 0, 
													0, dm.SoLuong_GhiNhan)
						   ,[SoLuongKMThayDoi] = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, dm.SoLuong_GhiNhan, 0)
						   ,[GiaTriKMLaiThayDoi] = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, dm.ThanhTienLai, 0)
			FROM #DmTinhLai_TheoOrder dm
			INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			OUTER APPLY (SELECT TOP 1 DmWebsiteReportingdbID, WebsiteLink
						 FROM ABM_Data_ThucChay.dbo.WebsiteMapping_HDCN_Reporting w 
						 WHERE w.DmWebsiteID = ISNULL(dm.DmWebsiteID, 265) ) w
			UNION ALL
			SELECT  	    tcdt.HopDongREF
						   ,tcdt.[SoHopDong] 
						   ,tcdt.[DmMaHopDongREF] 
						   ,tcdt.[NgayDanhSoHopDong]
						   ,tcdt.[TrangThaiHopDong]
						   ,tcdt.[DmNhanVienREF] 
						   ,tcdt.[TenDangNhap]   
						   ,tcdt.[DmPhongBanREF] 
						   ,tcdt.[DmBoPhanREF]
						   ,tcdt.[DmNhomLamViecREF]   
						   ,tcdt.[DmDiaDiemLamViecREF] 
						   ,tcdt.[DmKhachHangREF]  
						   ,tcdt.[HopDongChiTietREF]
						   ,tcdt.LstDmNhanHangREF
						   ,tcdt.[LstDmNhomNganhREF] 
						   ,tcdt.[DmHinhThucQuangCaoREF]    
						   ,tcdt.[DmSanPhamREF] 
						   ,tcdt.[DmChuyenMucREF] 
						   ,tcdt.[DmLoaiBannerREF] 
						   ,tcdt.[DmViTriREF] 
						   ,tcdt.[SoLuong] 
						   ,tcdt.[DonViTinhREF]      
						   ,tcdt.[DonGia]     
						   ,tcdt.[ChietKhau]   
						   ,tcdt.[ThanhTien] 
						   ,tcdt.[IsKhuyenMai]      
						   ,tcdt.[KhuyenMai]  
						   ,TongTienDuToanLaiMuaSauCK
						   ,tcdt.DmBannerREF 
						   ,tcdt.DmChienDichREF 
						   ,tcdt.DmWebsiteREF 
						   ,tcdt.TenWebsite
						   ,tcdt.DonViTinhThucChay
						   ,tcdt.DonGiaTheoDonViTinhTC 
						   ,[TongThanhTienThucChayBanSauCK] = 0
						   ,[TongThanhTienThucChayMuaSauCK] = 0				
						   ,[GiaTriThayDoiLaiSauCK] = -([GiaTriThayDoiLaiSauCK] + [ThanhTienLaiThucChaySauCK])
						   ,[SoLuongThayDoi] = -([SoLuongThayDoi] + tcdt.SoLuongThucChay)
						   ,[SoLuongKMThayDoi] = -([SoLuongKMThayDoi] + tcdt.SoLuongThucChayKM)
						   ,[GiaTriKMLaiThayDoi] = -([GiaTriKMLaiThayDoi] +ThanhTienLaiThucChayKM)
			FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh_MuaNgoai tcdt
			INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID
						FROM #DmPBThayDoi dm) dm ON dm.HopDongChiTietID = tcdt.HopDongChiTietREF
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien <= @NgayGhiNhan 
						AND (tcdt.DmSanPhamREF in (306,423,5160,5188,772)  OR tcdt.DmViTriREF in (100093,100478,100774) )
						AND tcdt.DmSanPhamREF <> 585
						AND NOT (tcdt.DmHinhThucQuangCaoREF IN(13) OR tcdt.DmLoaiBannerREF IN (18))
	) tcdt
	INNER JOIN (SELECT DISTINCT dm.HopDongChiTietID, 
								LyDo = N'phân bổ ' + CAST(dm.HopDongChiTietID AS NVARCHAR(50)) + N' có: ' + pb_LyDo.DsLyDo
				FROM #DmPBThayDoi dm
				JOIN (	SELECT dm1.HopDongChiTietID,
								STUFF((
									SELECT DISTINCT ';  ' + dm2.LyDo
									FROM #DmPBThayDoi dm2
									WHERE dm1.HopDongChiTietID = dm2.HopDongChiTietID
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS DsLyDo
						FROM #DmPBThayDoi dm1
						GROUP BY dm1.HopDongChiTietID
					) pb_LyDo ON dm.HopDongChiTietID = pb_LyDo.HopDongChiTietID
				) dm ON dm.HopDongChiTietID = tcdt.HopDongChiTietREF
	GROUP BY	HopDongREF,
				SoHopDong,
				DmMaHopDongREF,
				NgayDanhSoHopDong,
				TrangThaiHopDong,
				DmNhanVienREF,
				TenDangNhap,
				DmPhongBanREF,
				DmBoPhanREF,
				DmNhomLamViecREF,
				DmDiaDiemLamViecREF,
				DmKhachHangREF,
				HopDongChiTietREF,
				LstDmNhanHangREF,
				LstDmNhomNganhREF,
				DmHinhThucQuangCaoREF,
				DmSanPhamREF,
				DmChuyenMucREF,
				DmLoaiBannerREF,
				DmViTriREF,
				SoLuong,
				DonViTinhREF,
				DonGia,
				ChietKhau,
				ThanhTien,
				IsKhuyenMai,
				KhuyenMai,
				DmBannerREF,
				DmChienDichREF,
				DmWebsiteREF,
				TenWebsite,
				DonViTinhThucChay,
				DonGiaTheoDonViTinhTC,
				dm.LyDo
	HAVING SUM(tcdt.GiaTriThayDoiLaiSauCK ) <> 0
		   OR SUM(tcdt.GiaTriKMLaiThayDoi) <> 0
		   OR SUM(tcdt.SoLuongThayDoi) <> 0 
		   OR SUM(tcdt.SoLuongKMThayDoi) <> 0 

	--============================ UPDATE IsCalculate
	BEGIN
		UPDATE TC
		SET IsCaculatedActual = 0
		FROM dbo.[ADS_Operating_Result_Map_Order] TC
		INNER JOIN dbo.ADS_Operating_Order OD ON OD.ID = TC.Operating_Order_Id
		INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietID = OD.Contract_Detail_Id
		WHERE CAST(TC.LastModificationTime AS DATE) < @NgayGhiNhan OR 
		     (CAST(TC.LastModificationTime AS DATE) = @NgayGhiNhan AND TC.IsCaculatedActual = 1 AND 
			  TC.ID NOT IN (SELECT ID FROM #dmIDtinhmoi WHERE type = 1))

		UPDATE TC
		SET [IsCalc_Result_Quantity] = 0
		FROM dbo.[ADS_Operating_Result_Quantity] TC
		INNER JOIN dbo.ADS_Operating_Order OD ON OD.ID = TC.Operating_Order_Id
		INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietID = OD.Contract_Detail_Id
		WHERE CAST(TC.LastModificationTime AS DATE) < @NgayGhiNhan OR 
		     (CAST(TC.LastModificationTime AS DATE) = @NgayGhiNhan AND TC.IsCalc_Result_Quantity = 1 AND 
			  TC.ID NOT IN (SELECT ID FROM #dmIDtinhmoi WHERE type = 2))


		UPDATE TC
		SET IsCaculatedActual = 1
		FROM dbo.[ADS_Operating_Result_Map_Order] TC
		INNER JOIN #DmTinhLai_TheoOrder dm ON dm.type = 1 AND TC.Id = dm.ID

		UPDATE TC
		SET [IsCalc_Result_Quantity] = 1
		FROM dbo.[ADS_Operating_Result_Quantity] TC
		INNER JOIN #DmTinhLai_TheoOrder dm ON dm.type = 2 AND TC.Id = dm.ID

	END

	DROP TABLE #DmPBThayDoi
	DROP TABLE #DmTinhLai_TheoOrder
	DROP TABLE #dmIDtinhmoi

END 


```
